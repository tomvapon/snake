"""
In this file, the validators for board, snake and depth are implemented.
It is also check the valid movements
"""

from .snake_utils import get_new_head_from_movement


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


def depth_guarantee(depth):
    """
    Guarantee the depth is between 1 and 20 (included)

    :param depth: path depth
    :return: Boolean, True if depth is satisfied
    """

    return 1 <= depth <= 20


def guarantee_constraints(board, snake, depth):
    """
    This function checks the board, snake, board-snake and depth constraints.

    :param board: A 2D list for board dimensions
    :param snake: A 2D list of two-length arrays for snake dimensions
    :param depth: path depth
    :return: (Boolean, text): True if all constraints are fulfil
    """

    if not board_guarantee(board):
        return False, "Board {} does not satisfy constraints.".format(board)

    if not snake_guarantee(snake):
        return False, "Snake {} satisfies constraints.".format(snake)

    if not board_snake_guarantee(board, snake):
        return False, "Snake outbounds board."

    if not depth_guarantee(depth):
        return False, "Depth: {} is out of bounds.".format(depth)

    return True, "All constraints are satisfied!"


# Validate the snake movement
def is_valid_snake_head(head, board):
    """
    Checks if the head is valid in the bounds. For new heads
    :param head: the current snake head
    :param board: A 2D list for board dimensions
    :return:
    """

    return all([0 <= head[i] < board[i] for i in range(0, 2)])


def is_collapse_snake(snake):
    """
    Checks if the snake is collapsing against itself (current updated snake) -- Just check head
    :param snake: A 2D list of two-length arrays for snake dimensions
    :return: True if the snake is collapsing
    """

    return any([snake_dimension[0] == snake[0][0] and snake_dimension[1] == snake[0][1]
                for snake_dimension in snake[1:]])


def is_valid_movement(snake, board, movement):
    """
    This functions returns True if the snake movement is valid. No outbounds the board
    and do not collapse with itself.

    :param snake: A 2D list of two-length arrays for snake dimensions
    :param board: A 2D list for board dimensions
    :param movement: A valid movement ('L', 'R', 'U', 'D')
    :return: Bolean, True if the movement is valid
    """

    new_head = get_new_head_from_movement(snake[0], movement)

    # Check new head is valid (no out of bounds)
    if not is_valid_snake_head(new_head, board):
        return False

    # Check if configuration is valid, no collapse
    if is_collapse_snake([new_head] + snake[:-1]):
        return False

    # If reach this point the movement is valid
    return True
