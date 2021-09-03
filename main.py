"""
This is the main file of the snake algorithm
The problem is to be solve recursively based on
a backtracking algorithm. In each configuration (board, snake)
there are four possible movements (L, R, U, D). All options are
explore and invalid solutions are discard.
"""

import logic.validators as lv

# Example input
board = [4, 3]
snake = [[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]
depth = 3


if __name__ == '__main__':
    # Execute algorithm
    run = True
    if lv.board_guarantee(board):
        print("Board {} satisfies constraints.".format(board))
    else:
        print("Board {} does not satisfy constraints.".format(board))
        run = False

    if lv.snake_guarantee(snake):
        print("Snake {} satisfies constraints.".format(snake))
    else:
        print("Snake {} does not satisfy constraints.".format(snake))
        run = False

    if lv.board_snake_guarantee(board, snake):
        print("Board-snake satisfies constraints.".format(board))
    else:
        print("Snake outbounds board.".format(board))
        run = False

    if run:
        pass
    else:
        print("Algorithm execution aborted!")