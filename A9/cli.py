# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import *

df = pd.read_csv('./database.csv')

if __name__ == '__main__':

    player, winner, placement = 'X', None, False # 'X' goes first in tic-tac-toe

    mode = str(input("[1] for Single Player Mode, [2] for Two Player Mode. "))
    game = TicTacToe(mode)

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
            game.board_slots.remove(loc + 1)
            result = game.get_winner()

        # TODO: Update who's turn it is.
        if game.mode == '2':
            player = game.other_player(player)
            placement = False
        elif game.mode == '1' and len(game.board_slots) != 0: # Or ask the computer to finish its turn on a random block
            game.random_move()

        # Result
        result = game.get_winner()
            
        if result != None:
            df.loc[len(df.index)] = [int(game.mode), result]
            df.to_csv('./database.csv', index=False) # Record the game
            winning_times = df['result'].value_counts().tolist()[df['result'].value_counts().keys().tolist().index(result)]
            winning_rate = winning_times / len(df) * 100 # Calculate and display relevant statistics

            if result == 'X' or result == 'O':
                print("The winner is " + result + " ! The current winning rate is " + str(round(winning_rate, 2)) + " %.") 
                winner = True
            elif result == 'D':
                print(f"Draw! This only happens {winning_rate}% of the time.") 
                winner = True
        else:
            continue
