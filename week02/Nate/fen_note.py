def fen_to_description(fen):
    """
    Generate a natural language description of a chess position from FEN notation
    """
    # Define piece names and symbols
    piece_names = {
        'r': ('black rook', '♜'),
        'n': ('black horse', '♞'),
        'b': ('black bishop', '♝'),
        'q': ('black queen', '♛'),
        'k': ('black king', '♚'),
        'p': ('black pawn', '♟'),
        'R': ('white rook', '♖'),
        'N': ('white horse', '♘'),
        'B': ('white bishop', '♗'),
        'Q': ('white queen', '♕'),
        'K': ('white king', '♔'),
        'P': ('white pawn', '♙')
    }
    
    # File letters for coordinates
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    # Split FEN and get board position
    fen_parts = fen.split(' ')
    board_fen = fen_parts[0]
    
    # Parse the board
    pieces_by_type = {}
    
    rank = 8
    for row in board_fen.split('/'):
        file_index = 0
        for char in row:
            if char.isdigit():
                # Skip empty squares
                file_index += int(char)
            else:
                # Found a piece
                piece_info = piece_names[char]
                piece_name = piece_info[0]
                square = f"{files[file_index]}{rank}"
                
                if piece_name not in pieces_by_type:
                    pieces_by_type[piece_name] = []
                pieces_by_type[piece_name].append(square)
                file_index += 1
        rank -= 1
    
    # Generate description
    description_lines = []
    
    # Process pieces in a specific order for better readability
    piece_order = [
        'black queen', 'black rook', 'black king', 'black bishop', 'black horse',
        'white queen', 'white rook', 'white king', 'white bishop', 'white horse',
        'black pawn', 'white pawn'
    ]
    
    for piece_type in piece_order:
        if piece_type in pieces_by_type:
            squares = pieces_by_type[piece_type]
            if squares:
                color = 'black' if piece_type.startswith('black') else 'white'
                piece_name_simple = piece_type.replace('black ', '').replace('white ', '')
                
                if len(squares) == 1:
                    description_lines.append(f"{piece_type.capitalize()} is at {squares[0]}.")
                else:
                    squares_str = ", ".join(squares[:-1]) + f" and {squares[-1]}"
                    description_lines.append(f"{color.capitalize()} {piece_name_simple}s are at {squares_str}.")
    
    return "\n".join(description_lines)

def fen_to_detailed_description(fen):
    """
    Generate a more detailed description similar to the example
    """
    # Define piece names
    piece_names = {
        'r': 'black rook',
        'n': 'black horse',
        'b': 'black bishop',
        'q': 'black queen',
        'k': 'black king',
        'p': 'black pawn',
        'R': 'white rook',
        'N': 'white horse',
        'B': 'white bishop',
        'Q': 'white queen',
        'K': 'white king',
        'P': 'white pawn'
    }
    
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    
    # Parse FEN
    fen_parts = fen.split(' ')
    board_fen = fen_parts[0]
    
    # Group pieces by rank for more natural description
    pieces_by_rank = {8: [], 7: [], 6: [], 5: [], 4: [], 3: [], 2: [], 1: []}
    
    rank = 8
    for row in board_fen.split('/'):
        file_index = 0
        for char in row:
            if char.isdigit():
                file_index += int(char)
            else:
                piece_name = piece_names[char]
                square = f"{files[file_index]}{rank}"
                pieces_by_rank[rank].append((piece_name, square))
                file_index += 1
        rank -= 1
    
    # Generate description
    description_lines = []
    
    for rank in sorted(pieces_by_rank.keys(), reverse=True):
        pieces = pieces_by_rank[rank]
        if pieces:
            # Group pieces by type for this rank
            pieces_dict = {}
            for piece_name, square in pieces:
                if piece_name not in pieces_dict:
                    pieces_dict[piece_name] = []
                pieces_dict[piece_name].append(square)
            
            rank_description = []
            for piece_name, squares in pieces_dict.items():
                if len(squares) == 1:
                    rank_description.append(f"{piece_name} is at {squares[0]}")
                else:
                    squares_str = ", ".join(squares[:-1]) + f" and {squares[-1]}"
                    rank_description.append(f"{piece_name}s are at {squares_str}")
            
            if rank_description:
                description_lines.append(" ".join(rank_description) + ".")
    
    return "\n".join(description_lines)

# If he can generate the code to visualize the FEN notation maybe he can understand it better?
# as per giving it inside his system prompt to be the reference just like it is with Agents?
def create_chess_board(fen):
    """
    Create a chess board visualization from FEN notation
    """
    # Define piece mapping
    piece_symbols = {
        'r': '♜', 'R': '♖',
        'n': '♞', 'N': '♘',
        'b': '♝', 'B': '♗',
        'q': '♛', 'Q': '♕',
        'k': '♚', 'K': '♔',
        'p': '♟', 'P': '♙'
    }
    
    # Split FEN into parts and take only the board position
    fen_parts = fen.split(' ')
    board_fen = fen_parts[0]
    
    # Parse the FEN board notation
    board = []
    for row in board_fen.split('/'):
        board_row = []
        for char in row:
            if char.isdigit():
                # Add empty squares
                board_row.extend([' '] * int(char))
            else:
                # Add piece
                board_row.append(piece_symbols[char])
        board.append(board_row)
    
    # Create the board visualization
    output = []
    
    # Header row with letters
    header = "|   | " + " | ".join(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']) + " |"
    separator = "|---|---|---|---|---|---|---|---|---|"
    
    output.append(header)
    output.append(separator)
    
    # Board rows with numbers
    for i, row in enumerate(board):
        row_number = 8 - i
        row_str = f"| {row_number} | " + " | ".join(row) + " |"
        output.append(row_str)
    
    return "\n".join(output)

if __name__ == "__main__":
    # FEN notation for the given board position
    fen_notation = "r1b2rk1/ppp2p1p/1b1p1B2/5q1Q/2Bp4/2P5/PP3PPP/R3R1K1 w - - 0 1"
    # Generate and print the chess board
    print(create_chess_board(fen_notation))
    create_chess_board(fen_notation)
    print("=== Simple Description ===")
    print(fen_to_description(fen_notation))
    print("\n=== Detailed Description ===")
    print(fen_to_detailed_description(fen_notation))