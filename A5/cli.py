# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':
    board = make_empty_board()
    player, winner, placement = 'X', None, False # 'X' goes first in tic-tac-toe
    while winner == None:
        print("Turn for player '" + player + "'")
        
        # TODO: Show the board to the user.
        for row in board:
            print(row)

        # TODO: Input a move from the player.
        try:
            loc = int(input("Please choose which square to take. ")) - 1
        except ValueError:
            print("Please enter a number: ")

        if board[loc // 3][loc % 3] != None:
            print("The block is already taken, please choose another one.")
        else:
            placement = True

        # TODO: Update the board.
        if placement == True:
            board[loc // 3][loc % 3] = player

        # TODO: Update who's turn it is.
            player = other_player(player)
            placement = False


        # Result
        result = get_winner(board)

        if result == 'X' or result == 'O':
            print("The winner is " + result[0] + " !")
            winner = True
        elif result == 'D':
            print("Draw!")
        else:
            continue
