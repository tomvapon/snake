"""
In this file, the unit testing is to be implemented for validator and utils functions
"""

import unittest
import logic.validators as lv


class TestValidators(unittest.TestCase):

    def setUp(self):
        # SetUp with the example snake and board
        self.board = [4, 3]
        self.snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
        self.depth = 3

    def test_board_guarantee(self):
        # Assert true for the board
        self.assertTrue(lv.board_guarantee(self.board))

        # Assert false for invalid boards
        invalid_boards = [[4, 11], [1, 2, 3]]
        for invalid_board in invalid_boards:
            self.assertFalse(lv.board_guarantee(invalid_board))

    def test_snake_guarantee(self):
        # Assert true for the setUp snake
        self.assertTrue(lv.snake_guarantee(self.snake))

        # Assert false for invalid snakes
        invalid_snakes = [[[1, 2], [2, 3]], [[1, 2, 3], [3, 2], [3, 1], [3, 0]]]
        for invalid_snake in invalid_snakes:
            self.assertFalse(lv.snake_guarantee(invalid_snake))

    def test_board_snake_guarantee(self):
        # Assert true for the setUp snake and board
        self.assertTrue(lv.board_snake_guarantee(self.board, self.snake))

        # Assert false for outbounds snake
        invalid_snake = [[2, 2], [3, 2], [4, 1], [3, 0], [2, 0]]
        self.assertFalse(lv.board_snake_guarantee(self.board, invalid_snake))


# Main function to run the tests
if __name__ == '__main__':
    unittest.main()