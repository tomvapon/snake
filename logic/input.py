"""
This file implements the load input for the files
"""

import sys
import configparser


def load_input_file(file):
    """
    This function load an input file which contains the board dimensions, the snake and the depth.
    This simplifies the problem of manual console input and let check the three acceptance tests.

    :return: board (list), snake (list of lists), depth (int)
    """

    # Load config parser
    config = configparser.ConfigParser()

    # Read first argument (data file)
    config.read(file)

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

