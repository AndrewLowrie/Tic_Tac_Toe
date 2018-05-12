# The following is a simple game of tic tac toe for two players coded in Python.

import random

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

def win_check(board, mark):
    if (mark == board[0] and mark == board[1] and mark == board[2]):
        return True
    elif (mark == board[3] and mark == board[4] and mark == board[5]):
        return True
    elif (mark == board[6] and mark == board[7] and mark == board[8]):
        return True
    elif (mark == board[0] and mark == board[3] and mark == board[6]):
        return True
    elif (mark == board[1] and mark == board[4] and mark == board[7]):
        return True
    elif (mark == board[2] and mark == board[5] and mark == board[8]):
        return True
    elif (mark == board[0] and mark == board[4] and mark == board[8]):
        return True
    elif (mark == board[2] and mark == board[4] and mark == board[6]):
        return True
    else:
        return False

def choose_first():
    player_to_start = random.randint(1, 2)
    if (player_to_start == 1):
        return "Player 1"
    else:
        return "Player 2"
