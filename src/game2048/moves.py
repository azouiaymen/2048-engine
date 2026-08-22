from game2048.board import BOARD_SIZE


def move_row_left(row):
    values = []

    for cell in row:
        if cell is not None:
            values.append(cell)

    merged = []
    index = 0

    while index < len(values):
        if (
            index + 1 < len(values)
            and values[index] == values[index + 1]
        ):
            merged.append(values[index] * 2)
            index += 2
        else:
            merged.append(values[index])
            index += 1

    while len(merged) < BOARD_SIZE:
        merged.append(None)

    return merged


def move_left(board):
    new_board = []

    for row in board:
        new_board.append(move_row_left(row))

    return new_board


def move_row_right(row):
    reversed_row = list(reversed(row))
    moved_row = move_row_left(reversed_row)
    return list(reversed(moved_row))


def move_right(board):
    new_board = []

    for row in board:
        new_board.append(move_row_right(row))

    return new_board