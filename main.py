"""
This is the main file of the snake algorithm
The problem is to be solve recursively based on
a backtracking algorithm. In each configuration (board, snake)
there are four possible movements (L, R, U, D). All options are
explore and invalid solutions are discard.
"""

import logic.validators as lv

if __name__ == '__main__':
    # Example input
    board = [4, 3]
    snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
    depth = 3

    run, message = lv.guarantee_constraints(board, snake, depth)

    if run:
        print("Executing algorithm...")
        pass
    else:
        print(message)