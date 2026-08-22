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


def add_random_tile(board):
    new_board = []

    for row in board:
        new_board.append(row.copy())

    empty_cells = []

    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            if new_board[row][column] is None:
                empty_cells.append((row, column))

    if not empty_cells:
        return new_board

    row, column = random.choice(empty_cells)
    new_board[row][column] = random.choice([2, 4])

    return new_board