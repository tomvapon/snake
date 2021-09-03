"""
This is the main file of the snake algorithm
The problem is to be solve recursively based on
a backtracking algorithm. In each configuration (board, snake)
there are four possible movements (L, R, U, D). All options are
explore and invalid solutions are discard.
"""


import sys
import configparser
from logic.validators import guarantee_constraints
from logic.algorithm import explore_paths


def load_input_file():
    """
    This function load an input file which contains the board dimensions, the snake and the depth.
    This simplifies the problem of manual console input and let check the three acceptance tests.

    :return: board (list), snake (list of lists), depth (int)
    """

    # Load config parser
    config = configparser.ConfigParser()

    # Read first argument (data file)
    config.read(sys.argv[1])

    # Parse the inputs from string to its type
    # Board (str --> list)
    board_string = config['input']['board']
    input_board = [int(element) for element in board_string.split(',')]

    # Snake (str --> list of lists)
    snake_string = config['input']['snake']
    input_snake = [[int(el.split(',')[0]), int(el.split(',')[1])] for el in snake_string.split(';')]

    # Depth (str --> int)
    input_depth = int(config['input']['depth'])

    return input_board, input_snake, input_depth


if __name__ == '__main__':
    # Load the input from the files
    board, snake, depth = load_input_file()

    # Execute the guarantee of input
    run, message = guarantee_constraints(board, snake, depth)

    # Instantiate composed solution (final one)
    composed_solution = []

    if run:
        print("Executing algorithm...")
        # Execute the first iteration with the current solution empty and the initial configuration
        explore_paths(board, snake, depth, [], composed_solution)

        # The output is the length of the composed solution
        print(len(composed_solution))
    else:
        # Print error message in case input not guaranteed
        print(message)

