# The following is a simple game of tic tac toe for two players coded in Python.

def display_board(board):
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])

def player_input():
    player1 = ''

    # To ensure the player only chooses a valid marker.
    while (player1 != "X") and (player1 != "O"):
        player1 = input("Please choose 'X' or 'O': " )

    # Setting player two's marker.
    if (player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)

def place_marker(board, marker, position):
    position -= 1
    board[position] = marker
    return board
