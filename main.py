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
from logic.input import load_input_file


if __name__ == '__main__':
    # Load the input from the files
    board, snake, depth = load_input_file(sys.argv[1])

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

