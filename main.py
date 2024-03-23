import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def get_empty_positions(board):
    empty_positions = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == " ":
                empty_positions.append((row, col))
    return empty_positions

def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter row and column (1-3): ").split())
            row -= 1
            col -= 1
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter two integers.")

def ai_move(board, ai_symbol, player_symbol):
    empty_positions = get_empty_positions(board)

    # Try to win
    for row, col in empty_positions:
        board[row][col] = ai_symbol
        if check_winner(board, ai_symbol):
            return row, col
        board[row][col] = " "

    # Block opponent from winning
    for row, col in empty_positions:
        board[row][col] = player_symbol
        if check_winner(board, player_symbol):
            board[row][col] = ai_symbol
            return row, col
        board[row][col] = " "

    # Take center if available
    if (1, 1) in empty_positions:
        return 1, 1

    # Take a random corner if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        if corner in empty_positions:
            return corner

    # Take any available edge
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    random.shuffle(edges)
    for edge in edges:
        if edge in empty_positions:
            return edge

def play_game():
    board = [[" "]*3 for _ in range(3)]
    symbols = ['X', 'O']
    random.shuffle(symbols)
    player_symbol, ai_symbol = symbols

    print("You are", player_symbol)
    print("AI is", ai_symbol)

    print_board(board)

    while True:
        player_row, player_col = player_move(board)
        board[player_row][player_col] = player_symbol
        print_board(board)
        if check_winner(board, player_symbol):
            print("Congratulations! You won!")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

        print("AI is thinking...")
        ai_row, ai_col = ai_move(board, ai_symbol, player_symbol)
        board[ai_row][ai_col] = ai_symbol
        print_board(board)
        if check_winner(board, ai_symbol):
            print("AI wins! Better luck next time.")
            break
        if is_board_full(board):
            print("It's a tie!")
            break

play_game()
