import pandas as pd
import statistics
import os

# ---- CONFIG ----
INPUT_FILE = "deepseek_100.csv"
OUT_DIR = "a_category_summaries_fixed"
COMBINED_OUT = "category_summary_combined_fixed.csv"

# ---- LOAD DATA ----
df = pd.read_csv(INPUT_FILE, dtype=str)  # read as strings for robustness

# Keep only real call rows: Call# should be numeric; drop summary rows
if "Call#" in df.columns:
    df = df[pd.to_numeric(df["Call#"], errors="coerce").notna()].copy()

# Normalize column names (case-insensitive lookup)
cols_lower = {c.lower(): c for c in df.columns}

def get_col(*candidates):
    for c in candidates:
        if c.lower() in cols_lower:
            return cols_lower[c.lower()]
    return None

COL_PUZZLEID = get_col("PuzzleID", "puzzleid", "Puzzle Id", "puzzle_id")
COL_NORMALIZED = get_col("Normalized", "normalized")
COL_LATENCY = get_col("Latency", "latency", "Latency (s)")
COL_TOTAL_TOKENS = get_col("TotalTokens", "total_tokens", "Total Tokens")
COL_LEGAL = get_col("Legal", "legal")
COL_CORRECT = get_col("Correct", "correct")
COL_MOVE = get_col("Move", "move")
COL_ANSWER = get_col("Answer SAN", "answer_san")

# Convert numeric fields
df[COL_NORMALIZED] = pd.to_numeric(df[COL_NORMALIZED], errors="coerce")
if COL_LATENCY:
    df[COL_LATENCY] = pd.to_numeric(df[COL_LATENCY], errors="coerce")
if COL_TOTAL_TOKENS:
    df[COL_TOTAL_TOKENS] = pd.to_numeric(df[COL_TOTAL_TOKENS], errors="coerce")

# Normalize boolean-like columns
def to_bool_series(df, col):
    if col is None:
        return pd.Series([False]*len(df), index=df.index)
    s = df[col].astype(str).str.strip().str.lower()
    return s.isin(["true","1","yes","y","t"])

legal_series = to_bool_series(df, COL_LEGAL)
correct_series = to_bool_series(df, COL_CORRECT)

# If Correct column missing but we have Answer SAN and Move, compute correctness
if COL_CORRECT is None and COL_ANSWER and COL_MOVE:
    correct_series = (
        df[COL_MOVE].fillna("").astype(str).str.strip()
        == df[COL_ANSWER].fillna("").astype(str).str.strip()
    )

df["_legal_bool"] = legal_series
df["_correct_bool"] = correct_series

# ---- ASSIGN CATEGORIES ----
# Use order of unique PuzzleIDs: first 10 = Easy, next 10 = Medium, next 10 = Hard
unique_puzzles = list(df[COL_PUZZLEID].astype(str).dropna().unique())
categories_map = {}
for idx, pid in enumerate(unique_puzzles):
    if idx < 10:
        categories_map[pid] = "Easy"
    elif idx < 20:
        categories_map[pid] = "Medium"
    elif idx < 30:
        categories_map[pid] = "Hard"
    else:
        categories_map[pid] = "Extra"

df["Category"] = df[COL_PUZZLEID].astype(str).map(categories_map)

# ---- METRIC COMPUTATION ----
def compute_stats(group):
    vals = group[COL_NORMALIZED].dropna().tolist()
    legal_vals = group.loc[group["_legal_bool"], COL_NORMALIZED].dropna().tolist()
    total = len(group)
    illegal_pct = ((~group["_legal_bool"]).sum() / total * 100) if total > 0 else 0.0
    accuracy_pct = (group["_correct_bool"].sum() / total * 100) if total > 0 else 0.0
    avg_norm = statistics.mean(vals) if vals else 0.0
    std_norm = statistics.pstdev(vals) if len(vals) > 1 else 0.0
    mae = statistics.mean(abs(v - 0.5) for v in vals) if vals else 0.0
    mean_legal = statistics.mean(legal_vals) if legal_vals else 0.0
    avg_latency = group[COL_LATENCY].dropna().mean() if COL_LATENCY else None
    avg_tokens = group[COL_TOTAL_TOKENS].dropna().mean() if COL_TOTAL_TOKENS else None
    return {
        "Average Normalized Value": round(avg_norm, 6),
        "Standard Deviation": round(std_norm, 6),
        "Mean Absolute Error": round(mae, 6),
        "Illegal Moves (%)": round(illegal_pct, 4),
        "Puzzle Solving Accuracy (%)": round(accuracy_pct, 4),
        "Mean Value (Legal Moves Only)": round(mean_legal, 6),
        "Average Latency (s)": round(avg_latency, 6) if avg_latency is not None else None,
        "Average Tokens (total)": round(avg_tokens, 4) if avg_tokens is not None else None,
    }

category_stats = {}
for cat in ["Easy", "Medium", "Hard", "Extra"]:
    grp = df[df["Category"] == cat]
    if len(grp) == 0:
        continue
    category_stats[cat] = compute_stats(grp)

# ---- SAVE OUTPUTS ----
os.makedirs(OUT_DIR, exist_ok=True)

# Save per-category
for cat, stats in category_stats.items():
    pd.DataFrame([stats]).to_csv(os.path.join(OUT_DIR, f"{cat}_summary_fixed.csv"), index=False)

# Combined file (metrics as rows, categories as columns)
combined_df = pd.DataFrame(category_stats).T  # categories as rows
combined_df = combined_df.T                  # metrics as rows
combined_df.to_csv(COMBINED_OUT)

print(f"✅ Combined summary saved to {COMBINED_OUT}")
print(combined_df)
