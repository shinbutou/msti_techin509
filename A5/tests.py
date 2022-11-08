import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.get_winner(board), 'X')

    # TODO: Test all functions from logic.py!
    def test_make_empty_board(self):
        self.assertEqual(logic.make_empty_board)

    def test_other_player(self):
        player = 'X'
        self.assertEqual(logic.other_player(player))


if __name__ == '__main__':
    unittest.main()