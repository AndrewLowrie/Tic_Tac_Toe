# The following is a simple game of tic tac toe for two players coded in Python.

import random

def display_board(board):
    print(' ')
    print(board[1] + "|" + board[2] + "|" + board[3])
    print("-----")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-----")
    print(board[7] + "|" + board[8] + "|" + board[9])
    print(' ')

def player_input():
    player1 = ''
    while (player1 != 'X') and (player1 != 'O'):
        player1 = input("Please choose 'X' or 'O': ")

    if (player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    if (mark == board[1] and mark == board[2] and mark == board[3]):
        return True
    elif (mark == board[4] and mark == board[5] and mark == board[6]):
        return True
    elif (mark == board[7] and mark == board[8] and mark == board[9]):
        return True
    elif (mark == board[1] and mark == board[4] and mark == board[7]):
        return True
    elif (mark == board[2] and mark == board[5] and mark == board[8]):
        return True
    elif (mark == board[3] and mark == board[6] and mark == board[9]):
        return True
    elif (mark == board[1] and mark == board[5] and mark == board[9]):
        return True
    elif (mark == board[3] and mark == board[5] and mark == board[7]):
        return True
    else:
        return False

def choose_first():
    marker_to_start = random.randint(1, 2)
    if (marker_to_start == 1):
        return "X"
    else:
        return "O"

def space_check(board, position):
    return (board[position] == " ")

def full_board_check(board):
    for index in range(0, 8):
        if space_check(board, index):
            return False
    return True

def player_choice(board):
    accepted_choice = False
    while accepted_choice == False:
        position = int(input("Please enter your next position: "))
        if (space_check(board, position)):
            accepted_choice = True
            return position

def replay():
    choice = input("Do you want to play again? y/n: ")
    return (choice == "y")

# All required functions listed above, game logic to be played follows below.
while True:

    board = [ ' ' ] * 10
    player1, player2 = player_input()
    player_to_start = choose_first()
    print(player_to_start + " will start.")

    game_won = False
    while game_won == False:

        # Game logic for player1 to start
        if player1 == player_to_start:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1, position)

            if win_check(board, player1):
                display_board(board)
                print("Congrats player 1!!!")
                game_won = True

            if full_board_check(board):
                display_board(board)
                print("It's a draw!")
                game_won = True

            player_to_start = player2

        # Game logic for player two to start, exact same as player one.
        # Simply repeats the same methods until there is a winner or a draw.
        if player2 == player_to_start:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2, position)

            if win_check(board, player2):
                display_board(board)
                print("Congrats player 2!!!")
                game_won = True

            if full_board_check(board):
                display_board(board)
                print("It's a draw!")
                game_won = True

            player_to_start = player1

    if replay() != True:
        break
