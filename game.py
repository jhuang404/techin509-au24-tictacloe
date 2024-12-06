import numpy as np
board = np.full((3, 3), ' ')
players = ["X", "O"]
turn=0

def check_winner(board):
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != ".":  # Rows
            return board[i, 0]
        if board[0, i] == board[1, i] == board[2, i] != ".":  # Columns
            return board[0, i]
    if board[0, 0] == board[1, 1] == board[2, 2] != ".":  # Main diagonal
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != ".":  # Anti-diagonal
        return board[0, 2]
    return None

while True:
    print_board(board)
    user_move = input(f"Player {players[turn]}'s turn. Please enter your move as x,y coordinates (e.g., 1,2): ")
    print(f"You entered: {user_move}")
    try:
        x, y = map(int, user_move.split(","))
    except ValueError:
        print("Invalid input format. Please try again!")
        continue

    if 0 <= x < 3 and 0 <= y < 3 and board[x, y] == ".":
          board[x, y] = players[turn]
        if check_winner(board):
             print_board(board)
             print(f"Player {players[turn]} wins!")
             break
        elif "." not in board:
             print_board(board)
             print("It's a draw!")
             break
        turn = 1 - turn
    else:
        print("Invalid move. Please try again!")
