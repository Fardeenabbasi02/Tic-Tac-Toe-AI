import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * 13)

# Check if there is a winner or draw
def check_winner(board):
    # Check rows, columns, and diagonals
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # Check if board is full (draw)
    for row in board:
        if " " in row:
            return None
    return "Draw"

# Minimax algorithm implementation
def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == "X":
        return -1
    elif winner == "O":
        return 1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

# Get the best move for AI (O)
def best_move(board):
    best_score = -math.inf
    move = (0, 0)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# Play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    human_turn = True  # X is human, O is AI

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            if winner == "Draw":
                print("It's a draw!")
            else:
                print(f"{winner} wins!")
            break

        if human_turn:
            print("Your turn (X)")
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter col (0, 1, or 2): "))
            if board[row][col] == " ":
                board[row][col] = "X"
                human_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            print("AI's turn (O)")
            row, col = best_move(board)
            board[row][col] = "O"
            human_turn = True

if _name_ == "_main_":
    play_game()