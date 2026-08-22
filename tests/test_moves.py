from game2048.moves import move_left


def test_move_left():
    board = [
        [None, 8, 2, 2],
        [4, 2, None, 2],
        [None, None, None, None],
        [None, None, None, 2],
    ]

    expected = [
        [8, 4, None, None],
        [4, 4, None, None],
        [None, None, None, None],
        [2, None, None, None],
    ]

    result = move_left(board)

    assert result == expected


def test_move_left_merges_each_tile_once():
    board = [
        [2, 2, 2, 2],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    result = move_left(board)

    assert result[0] == [4, 4, None, None]