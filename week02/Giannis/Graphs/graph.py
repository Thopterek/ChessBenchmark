import pandas as pd
import matplotlib.pyplot as plt

# Read markdown file
with open("data.md", "r") as f:
    text = f.read()

# Pandas can read markdown tables if we extract them
from io import StringIO

# Extract the table part (skip the text above if needed)
table_text = """
| Month   | Sales |
|---------|-------|
| Jan     | 100   |
| Feb     | 120   |
| Mar     | 90    |
| Apr     | 150   |
| May     | 200   |
"""

df = pd.read_csv(StringIO(table_text), sep="|", engine="python")

# Clean column names and rows (because of extra whitespace)
df = df.dropna(axis=1, how="all")   # remove empty columns
df.columns = [c.strip() for c in df.columns]
df = df.applymap(lambda x: str(x).strip())

# Convert Sales to int
df["Sales"] = df["Sales"].astype(int)

# Plot
plt.plot(df["Month"], df["Sales"], marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

