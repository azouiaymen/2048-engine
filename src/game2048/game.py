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



def has_won(board):
    for row in board:
        for cell in row:
            if cell is not None and cell >= 2048:
                return True

    return False

def has_available_move(board):
    # If there is an empty cell, the game is not over
    for row in board:
        if None in row:
            return True

    # Board is full, so check whether any direction can still change it
    if move_left(board) != board:
        return True

    if move_right(board) != board:
        return True

    if move_up(board) != board:
        return True

    if move_down(board) != board:
        return True

    return False


def get_game_status(board):
    if has_won(board):
        return "won"

    if not has_available_move(board):
        return "lost"

    return "playing"
