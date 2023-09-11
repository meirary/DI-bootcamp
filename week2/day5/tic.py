def display_board(board):
    """Display the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def player_input(player):
    """Get the position from the player."""
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0, 1, 2): "))
            col = int(input(f"Player {player}, enter column (0, 1, 2): "))
            if 0 <= row < 3 and 0 <= col < 3:
                return row, col
            else:
                print("Invalid input. Please enter valid row and column.")
        except ValueError:
            print("Invalid input. Please enter valid row and column.")

def check_win(board, player):
    """Check whether there is a winner or not."""
    # Check rows
    for row in board:
        if all(mark == player for mark in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def play():
    """The main function to play the game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"

    for _ in range(9):
        display_board(board)
        row, col = player_input(player)

        if board[row][col] == " ":
            board[row][col] = player
        else:
            print("That position is already occupied. Try again.")
            continue

        if check_win(board, player):
            display_board(board)
            print(f"Player {player} wins!")
            break

        player = "O" if player == "X" else "X"
    else:
        display_board(board)
        print("It's a tie!")

if __name__ == "__main__":
    play()
