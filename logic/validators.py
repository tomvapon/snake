"""
In this file, the validators for board, snake and depth are implemented.
It is also check the valid movements
"""

# First the guarantee constraint are implemented
def board_guarantee(board):
    """
    Guarantee the board dimensions (2D) and 1 <= n <= 10

    :param board: A 2D list for board dimensions
    :return: Boolean, True if board is valid
    """

    return len(board) == 2 and all([1 <= board_dimension <= 10 for board_dimension in board])


def snake_guarantee(snake):
    """
    Guarantee the snake dimensions (2D) and 3 <= n <= 7

    :param snake: A 2D list of two-length arrays for snake dimensions
    :return: Boolean, True if snake is valid
    """

    return 3 <= len(snake) <= 7 and all([len(elem) == 2 for elem in snake])


def board_snake_guarantee(board, snake):
    """
    Guarantee the snake fits in the board

    :param board: A 2D list for board dimensions
    :param snake: A 2D list of two-length arrays for snake dimensions
    :return: Boolean, True if snake fits in the board
    """

    return all([0 <= snake_piece[i] < board[i] for i in range(0, 2) for snake_piece in snake])