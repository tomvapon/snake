"""
In this file, the unit testing is to be implemented for validator and utils functions
"""

import unittest
import logic.validators as lv
import logic.snake_utils as ls
from logic.input import load_input_file
from logic.validators import guarantee_constraints
from logic.algorithm import explore_paths


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

    def test_depth_guarantee(self):
        # Assert setUp depth is correct
        self.assertTrue(lv.depth_guarantee(self.depth))

        # Negative depth and outbound depth
        invalid_depths = [-3, 25]
        for invalid_depth in invalid_depths:
            self.assertFalse(lv.depth_guarantee(invalid_depth))

    def test_is_valid_snake_head(self):
        # Assert true for the board
        head = [3, 2]
        bad_head = [2, 4]
        self.assertTrue(lv.is_valid_snake_head(head, self.board))
        self.assertFalse(lv.is_valid_snake_head(bad_head, self.board))

    def test_is_collapse_snake(self):
        # Assert true with initial snake
        self.assertFalse(lv.is_collapse_snake(self.snake))

        # Collapse with invalid movement, for example 'R'
        new_head = ls.get_new_head_from_movement(self.snake[0], 'R')
        self.assertTrue(lv.is_collapse_snake([new_head] + self.snake[:-1]))

    def test_is_valid_movement(self):
        # Assert true for up or left
        self.assertTrue(lv.is_valid_movement(self.snake, self.board, 'U'))
        self.assertTrue(lv.is_valid_movement(self.snake, self.board, 'L'))

        # Assert false for down or right
        self.assertFalse(lv.is_valid_movement(self.snake, self.board, 'D'))
        self.assertFalse(lv.is_valid_movement(self.snake, self.board, 'R'))


class TestSnakeUtils(unittest.TestCase):
    def setUp(self):
        self.board = [4, 3]
        self.snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
        self.depth = 3

    def test_get_new_head_from_movement(self):
        # Assert the correct position
        self.assertEqual(ls.get_new_head_from_movement(self.snake[0], 'R'), [3, 2])
        self.assertEqual(ls.get_new_head_from_movement(self.snake[0], 'L'), [1, 2])
        self.assertEqual(ls.get_new_head_from_movement(self.snake[0], 'U'), [2, 1])
        self.assertEqual(ls.get_new_head_from_movement(self.snake[0], 'D'), [2, 3])


class TestAcceptanceTests(unittest.TestCase):
    def test_acceptance_test_1(self):
        file = 'test_files/test1.txt'
        composed_solution = []
        board, snake, depth = load_input_file(file)

        # Execute the guarantee of input
        self.assertTrue(guarantee_constraints(board, snake, depth))

        # Execute the algorithm
        explore_paths(board, snake, depth, [], composed_solution)

        # Assert the length
        self.assertEqual(len(composed_solution), 7)

    def test_acceptance_test_2(self):
        file = 'test_files/test2.txt'
        composed_solution = []
        board, snake, depth = load_input_file(file)

        # Execute the guarantee of input
        self.assertTrue(guarantee_constraints(board, snake, depth))

        # Execute the algorithm
        explore_paths(board, snake, depth, [], composed_solution)

        # Assert the length
        self.assertEqual(len(composed_solution), 1)

    def test_acceptance_test_3(self):
        file = 'test_files/test3.txt'
        composed_solution = []
        board, snake, depth = load_input_file(file)

        # Execute the guarantee of input
        self.assertTrue(guarantee_constraints(board, snake, depth))

        # Execute the algorithm
        explore_paths(board, snake, depth, [], composed_solution)

        # Assert the length
        self.assertEqual(len(composed_solution), 81)


# Main function to run the tests
if __name__ == '__main__':
    unittest.main()


