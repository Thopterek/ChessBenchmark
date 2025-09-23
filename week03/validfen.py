import chess

input_file = "400k-cleaned-x.txt"
output_file = "valid_fens.txt"
invalid_file = "invalid_fens.txt"

valid_count = 0
invalid_count = 0

with open(input_file, "r") as infile, \
     open(output_file, "w") as outfile, \
     open(invalid_file, "w") as badfile:

    for line in infile:
        fen = line.strip()
        if not fen:
            continue
        try:
            board = chess.Board(fen)  # try to parse the FEN
            outfile.write(fen + "\n")
            valid_count += 1
        except Exception as e:
            badfile.write(fen + "\n")
            invalid_count += 1

print(f"✅ Valid FENs: {valid_count}")
print(f"❌ Invalid FENs: {invalid_count}")
print(f"Results saved to {output_file}, invalid ones in {invalid_file}")
