from game2048.board import add_random_tile
from game2048.moves import move_left, move_right, move_up, move_down


def play_move(board, direction):
    if direction == "left":
        moved_board = move_left(board)
    elif direction == "right":
        moved_board = move_right(board)
    elif direction == "up":
        moved_board = move_up(board)
    elif direction == "down":
        moved_board = move_down(board)
    else:
        raise ValueError("Invalid direction")

    if moved_board == board:
        return board

    return add_random_tile(moved_board)