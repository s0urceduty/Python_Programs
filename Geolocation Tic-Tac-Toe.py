import folium

# Create a Tic-Tac-Toe board on a map
def create_board():
    # Create a map centered around a specific location
    m = folium.Map(location=[latitude, longitude], zoom_start=15)

    # Create a grid of squares for the Tic-Tac-Toe board
    for row in range(3):
        for col in range(3):
            square = folium.Rectangle(
                bounds=[[latitude - 0.001 * row, longitude - 0.001 * col], 
                        [latitude - 0.001 * (row + 1), longitude - 0.001 * (col + 1)]],
                fill=True,
                color='blue',
                fill_color='blue',
                fill_opacity=0.6
            )

            square.add_to(m)

    return m

# Main game loop
def play_game():
    board = create_board()
    player = 'X'

    while True:
        print_board(board)

        # Get the player's move coordinates
        row = int(input(f"Enter the row (0-2) for '{player}': "))
        col = int(input(f"Enter the column (0-2) for '{player}': "))

        # Update the board
        if is_valid_move(board, row, col):
            update_board(board, row, col, player)

            if check_win(board, player):
                print_board(board)
                print(f"'{player}' wins!")
                break
            elif check_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

# Check if the move is valid
def is_valid_move(board, row, col):
    return board[row][col] == ' '

# Update the board with the player's move
def update_board(board, row, col, player):
    board[row][col] = player

# Check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == player) or \
           (board[0][i] == board[1][i] == board[2][i] == player):
            return True
    if (board[0][0] == board[1][1] == board[2][2] == player) or \
       (board[0][2] == board[1][1] == board[2][0] == player):
        return True
    return False

# Check if the game is a draw
def check_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Print the current state of the board
def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

if __name__ == "__main__":
    latitude = 40.7128  # Example latitude
    longitude = -74.0060  # Example longitude
    board = [[' ' for _ in range(3)] for _ in range(3)]
    play_game()
