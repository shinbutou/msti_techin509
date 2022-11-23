# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.

import pandas as pd # Using pandas for transposing
import random

class TicTacToe:
    board_size = '3*3'

    def __init__(self):
        self.board = [
            [None, None, None],
            [None, None, None],
            [None, None, None]
        ]

    def get_winner(self) -> str:
        # Row
        for i in range(3): # if a winner is a achieved in a row
            if len(set(self.board[i])) == 1:
                return self.board[i][0]

        # Column
        df = pd.DataFrame(self.board).T.values.tolist()
        print(df)
        for i in range(3): # if a winner is a achieved in a column (same logic with the original grid transposed)
            if len(set(df[i])) == 1:
                return df[i][0]

        # Checking the diagonal from top-left to bottom-right
        i, j, k = 0, 0, []
        for m in range(3):
            k.append(self.board[i][j])
            i += 1
            j += 1
        if len(set(k)) == 1:
            return k[0]

        # Checking the diagonal from bottom-left to top-right
        i, j, k = 2, 0, []
        for m in range(3):
            k.append(self.board[i][j])
            i -= 1
            j += 1
        if len(set(k)) == 1:
            return k[0]

        # Checking if there is a draw of if the game is still on
        check = []
        for i in range(3):
            for j in range(3):
                check.append(self.board[i][j])
        
        if None in set(check):
            print("The game is still on.")
            return None
        else:
            return 'D'


    def other_player(self, player):
        if player == 'X':
            return 'O'
        else:
            return 'X'

    def random_move(self):
        return random.randint(1, 9)