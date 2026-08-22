import random


BOARD_SIZE = 4
MIN_INITIAL_TILES = 2
MAX_INITIAL_TILES = 8


def create_board():
    board = []

    for _ in range(BOARD_SIZE):
        board.append([None] * BOARD_SIZE)

    number_of_twos = random.randint(MIN_INITIAL_TILES, MAX_INITIAL_TILES)
    placed = 0

    while placed < number_of_twos:
        row = random.randint(0, BOARD_SIZE - 1)
        column = random.randint(0, BOARD_SIZE - 1)

        if board[row][column] is None:
            board[row][column] = 2
            placed += 1

    return board