from game2048.ai import suggest_move


def test_ai_suggests_a_valid_move():
    board = [
        [None, 2, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    suggestion = suggest_move(board)

    assert suggestion in ["left", "right", "up", "down"]

def test_ai_returns_none_when_no_move_exists():
    board = [
        [2, 4, 2, 4],
        [4, 2, 4, 2],
        [2, 4, 2, 4],
        [4, 2, 4, 2],
    ]

    suggestion = suggest_move(board)

    assert suggestion is None