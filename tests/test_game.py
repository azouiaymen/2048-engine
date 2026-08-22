from game2048.game import play_move, get_game_status

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


def test_game_is_won_when_2048_is_reached():
    board = [
        [4, None, None, 2],
        [2048, None, None, None],
        [4, 2, None, None],
        [4, None, None, None],
    ]

    assert get_game_status(board) == "won"


def test_game_is_lost_when_no_moves_are_available():
    board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]

    assert get_game_status(board) == "lost"


def test_full_board_with_possible_merge_is_still_playing():
    board = [
        [2, 2, 4, 8],
        [4, 8, 16, 32],
        [8, 16, 32, 64],
        [16, 32, 64, 128],
    ]

    assert get_game_status(board) == "playing"