# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

if __name__ == '__main__':

    game = TicTacToe()
    player, winner, placement = 'X', None, False # 'X' goes first in tic-tac-toe

    while winner == None:
        print("Turn for player '" + player + "'")
        
        # TODO: Show the board to the user.
        for row in game.board:
            print(row)

        # TODO: Input a move from the player.
        try:
            loc = int(input("Please choose which square to take. ")) - 1
        except ValueError:
            loc = int(input("Please enter a number. ")) - 1 # This can only prevent an error once

        if loc < 0 or loc > 8:
            loc = int(input("Please choose a number from 1 to 9. ")) - 1 # This can only prevent an error once

        if game.board[loc // 3][loc % 3] != None:
            print("The block is already taken, please choose another one.")
        else:
            placement = True

        # TODO: Update the board.
        if placement == True:
            game.board[loc // 3][loc % 3] = player

        # TODO: Update who's turn it is.
            player = game.other_player(player)
            placement = False

        # Result
        result = game.get_winner()

        if result == 'X' or result == 'O':
            print("The winner is " + result + " !")
            winner = True
        elif result == 'D':
            print("Draw!")
            winner = True
        else:
            continue
