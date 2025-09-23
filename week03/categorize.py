import chess
import chess.engine

# Path to Stockfish
STOCKFISH_PATH = "/Users/salvador.dali.disciple/homebrew/bin/stockfish"
engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)


def normalize_fen(fen: str) -> str:
    """
    Ensure FEN has 6 fields. If only piece placement is given,
    assume: white to move, no castling, no en passant, halfmove=0, fullmove=1.
    """
    parts = fen.strip().split()
    if len(parts) == 1:  # only board layout
        return fen.strip() + " w - - 0 1"
    return fen.strip()


def evaluate_fen(fen, depth=12):
    """Return eval scores for best and second-best moves."""
    board = chess.Board(fen)

    # Ask Stockfish for top 2 moves
    info = engine.analyse(board, chess.engine.Limit(depth=depth), multipv=2)

    if not info:
        return None, None, None

    best = info[0]["score"].white()
    second = info[1]["score"].white() if len(info) > 1 else None
    return best, second, info


def difficulty_score(best, second):
    """
    Assign difficulty 1–10 based on eval difference and mate depth.
    Lower = easier, higher = harder.
    """
    if best.is_mate():
        mate_depth = abs(best.mate())
        if mate_depth == 1:
            return 1
        elif mate_depth <= 3:
            return 3
        elif mate_depth <= 5:
            return 5
        else:
            return 7

    if second is None:
        return 2  # trivial, only one good move found

    best_cp = best.score(mate_score=100000)
    second_cp = second.score(mate_score=100000)
    diff = abs(best_cp - second_cp)

    if diff > 500:
        return 2
    elif diff > 200:
        return 4
    elif diff > 100:
        return 6
    elif diff > 50:
        return 8
    else:
        return 10


def categorize_file(input_file):
    easy, medium, hard = [], [], []

    with open(input_file, "r") as f:
        for line in f:
            fen_raw = line.strip()
            if not fen_raw:
                continue

            try:
                fen = normalize_fen(fen_raw)
                best, second, _ = evaluate_fen(fen, depth=12)
                if best is None:
                    continue
                score = difficulty_score(best, second)

                if score <= 3:
                    easy.append(fen)
                elif score <= 7:
                    medium.append(fen)
                else:
                    hard.append(fen)

            except Exception as e:
                print(f"⚠️ Error on FEN {fen_raw}: {e}")
                continue

    with open("easy.txt", "w") as f: f.write("\n".join(easy))
    with open("medium.txt", "w") as f: f.write("\n".join(medium))
    with open("hard.txt", "w") as f: f.write("\n".join(hard))

    print(f"✅ Done! Easy: {len(easy)}, Medium: {len(medium)}, Hard: {len(hard)}")


if __name__ == "__main__":
    categorize_file("cleaned.txt")
    engine.quit()
