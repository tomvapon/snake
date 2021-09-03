"""
This is the main file of the snake algorithm
The problem is to be solve recursively based on
a backtracking algorithm. In each configuration (board, snake)
there are four possible movements (L, R, U, D). All options are
explore and invalid solutions are discard.
"""

import logic.validators as lv
from logic.validators import is_valid_movement
from logic.snake_utils import get_new_head_from_movement


# Constants
MOVEMENTS = ('L', 'U', 'D', 'R')

# Global solution (empty when instance)
solution = []


# Recursive function for solving the problem --> backtracking strategy
def explore_paths(board, snake, depth, current_solution):
    """
    This functions implements the recursive logic. For each configuration (snake/board), the four
    different movements is explored in order to reach a new valid solution or not.

    :param board: A 2D list for board dimensions
    :param snake: A 2D list of two-length arrays for snake dimensions
    :param depth: path depth
    :param current_solution: individual solution for the iteration
    :return:
    """

    # Check if the current solution is already a full solution
    if len(current_solution) == depth:
        # Add the current solution to the global solution vector
        solution.append(current_solution)
    else:
        # We explore the four possible movements
        for movement in MOVEMENTS:
            # Check if the movement is valid
            if is_valid_movement(snake, board, movement):
                # If it is valid, recursion is applied.
                # The new snake is calculated adding the head and cutting the tail
                new_snake = [get_new_head_from_movement(snake[0], movement)] + snake[:-1]
                new_current_solution = current_solution + [movement]
                explore_paths(board, new_snake, depth, new_current_solution)


if __name__ == '__main__':
    # Example input
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3

    run, message = lv.guarantee_constraints(board, snake, depth)

    if run:
        print("Executing algorithm...")
        # Execute the first iteration with the current solution empty and the initial configuration
        explore_paths(board, snake, depth, [])
        print(len(solution))
    else:
        print(message)