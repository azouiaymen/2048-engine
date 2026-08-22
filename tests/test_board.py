from game2048.board import (
    BOARD_SIZE,
    MIN_INITIAL_TILES,
    MAX_INITIAL_TILES,
    create_board,
)


def test_board_has_correct_size():
    board = create_board()

    assert len(board) == BOARD_SIZE

    for row in board:
        assert len(row) == BOARD_SIZE


def test_board_contains_only_twos_or_none():
    board = create_board()

    for row in board:
        for cell in row:
            assert cell is None or cell == 2


def test_board_has_valid_number_of_twos():
    board = create_board()

    number_of_twos = 0

    for row in board:
        for cell in row:
            if cell == 2:
                number_of_twos += 1

    assert MIN_INITIAL_TILES <= number_of_twos <= MAX_INITIAL_TILES