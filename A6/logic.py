# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import pandas as pd # Using pandas for transposing 

class TicTacToe:

    board_size = '3*3'

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
    
'''
    def make_empty_board():
        return [
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]
'''

    def get_winner(board) -> str:
        # Row
        for i in range(3): # if a winner is a achieved in a row
            if len(set(board[i])) == 1:
                return board[i][0], 

        # Column
        df = pd.DataFrame(board).T.values.tolist() 
        for i in range(3): # if a winner is a achieved in a column (same logic with the original grid transposed)
            if len(set(df[i])) == 1:
                return df[i][0]

        # Checking the diagonal from top-left to bottom-right
        i, j, k = 0, 0, []
        for m in range(3):
            k.append(board[i][j])
            i += 1
            j += 1
        if len(set(k)) == 1:
            return k[0]

        # Checking the diagonal from bottom-left to top-right
        i, j, k = 2, 0, []
        for m in range(3):
            k.append(board[i][j])
            i -= 1
            j += 1
        if len(set(k)) == 1:
            return k[0]

        # Checking if there is a draw of if the game is still on
        check = []
        for i in range(3):
            for j in range(3):
                check.append(board[i][j])
        
        if None in set(check):
            print("The game is still on.")
            return None
        else:
            return 'D'


    def other_player(player):
        if player == 'X':
            return 'O'
        else:
            return 'X'