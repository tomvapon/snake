"""
In this file, some util functions for snake logic are implemented.
"""


def get_new_head_from_movement(head, movement):
    """
    This functions returns the new head position according to the snake movement.

    :param head: 2D array for head current head position (snake[0])
    :param movement: A valid movement ('L', 'R', 'U', 'D')
    :return: new head: 2D array for head new head position
    """

    if movement == 'L':
        new_head = [head[0] - 1, head[1]]
    elif movement == 'R':
        new_head = [head[0] + 1, head[1]]
    elif movement == 'U':
        new_head = [head[0], head[1] - 1]
    else:
        new_head = [head[0], head[1] + 1]

    return new_head
