from game2048.moves import (
    move_left,
    move_right,
    move_up,
    move_down,
)


MOVES = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down,
}


def score_board(board):
    empty_cells = 0
    highest_tile = 0

    for row in board:
        for cell in row:
            if cell is None:
                empty_cells += 1
            elif cell > highest_tile:
                highest_tile = cell

    return empty_cells * 100 + highest_tile


def suggest_move(board):
    best_move = None
    best_score = -1

    for direction, move_function in MOVES.items():
        moved_board = move_function(board)

        # Ignore moves that do nothing
        if moved_board == board:
            continue

        score = score_board(moved_board)

        if score > best_score:
            best_score = score
            best_move = direction

    return best_move