
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 9)


def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True

        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


board = [[" " for _ in range(3)] for _ in range(3)]

current_player = "X"

for turn in range(9):
    print(f"\nPlayer {current_player}'s turn:")
    print_board(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    if board[row][col] == " ":
        board[row][col] = current_player

        if check_winner(board):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"

    else:
        print("Cell already occupied. Try again.")

else:
    print_board(board)
    print("\nGame Draw!")




# OUTPUT:
# Player X's turn:
#  | | 
# ---------
#  | | 
# ---------
#  | | 
# ---------
# Enter row (0-2): 0
# Enter column (0-2): 0

# Player O's turn:
# X| | 
# ---------
#  | | 
# ---------
#  | | 
# ---------
# Enter row (0-2): 1
# Enter column (0-2): 0

# Player X's turn:
# X| | 
# ---------
# O| | 
# ---------
#  | | 
# ---------
# Enter row (0-2): 0
# Enter column (0-2): 1

# Player O's turn:
# X|X| 
# ---------
# O| | 
# ---------
#  | | 
# ---------
# Enter row (0-2): 1
# Enter column (0-2): 1

# Player X's turn:
# X|X| 
# ---------
# O|O| 
# ---------
#  | | 
# ---------
# Enter row (0-2): 0
# Enter column (0-2): 2

# X|X|X
# ---------
# O|O| 
# ---------
#  | | 
# ---------

# Player X wins!