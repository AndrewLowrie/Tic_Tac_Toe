# The following is a simple game of tic tac toe for two players coded in Python.

def display_board(board):
    print(board[0][0] + "|" + board[0][1] + "|" + board[0][2])
    print("-----")
    print(board[1][0] + "|" + board[1][1] + "|" + board[1][2])
    print("-----")
    print(board[2][0] + "|" + board[2][1] + "|" + board[2][2])

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
