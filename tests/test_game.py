from game2048.game import play_move


def test_valid_move_adds_one_tile():
    board = [
        [None, 2, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    result = play_move(board, "left")

    filled_cells = 0

    for row in result:
        for cell in row:
            if cell is not None:
                filled_cells += 1

    assert filled_cells == 2


def test_invalid_move_does_not_add_tile():
    board = [
        [2, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    result = play_move(board, "left")

    assert result == board


def test_new_tile_is_two_or_four():
    board = [
        [None, 2, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    result = play_move(board, "left")

    for row in result:
        for cell in row:
            if cell is not None:
                assert cell in [2, 4]