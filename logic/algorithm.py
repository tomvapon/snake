"""
This file implements the algorithm logic to compute the solution. A priori, a backtracking
strategy is to be implemented.
"""

from .validators import is_valid_movement
from .snake_utils import get_new_head_from_movement

# Movement constants
MOVEMENTS = ('L', 'U', 'D', 'R')


# Recursive function for solving the problem --> backtracking strategy
def explore_paths(board, snake, depth, current_solution, composed_solution):
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
        composed_solution.append(current_solution)
    else:
        # We explore the four possible movements
        for movement in MOVEMENTS:
            # Check if the movement is valid
            if is_valid_movement(snake, board, movement):
                # If it is valid, recursion is applied.
                # The new snake is calculated adding the head and cutting the tail
                new_snake = [get_new_head_from_movement(snake[0], movement)] + snake[:-1]
                new_current_solution = current_solution + [movement]
                explore_paths(board, new_snake, depth, new_current_solution, composed_solution)