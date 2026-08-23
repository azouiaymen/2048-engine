from dotenv import load_dotenv
import os

from openai import OpenAI

from game2048.moves import (
    move_left,
    move_right,
    move_up,
    move_down,
)


load_dotenv()


MOVES = {
    "left": move_left,
    "right": move_right,
    "up": move_up,
    "down": move_down,
}


def get_valid_moves(board):
    valid_moves = []

    for direction, move_function in MOVES.items():
        moved_board = move_function(board)

        if moved_board != board:
            valid_moves.append(direction)

    return valid_moves


def suggest_move(board):
    valid_moves = get_valid_moves(board)

    if not valid_moves:
        return None

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise RuntimeError(
            "OPENAI_API_KEY environment variable is not set."
        )

    client = OpenAI(api_key=api_key)

    prompt = f"""
You are playing the game 2048.

Current board:
{board}

Valid moves:
{valid_moves}

Choose the best possible move to:
1. Avoid game over.
2. Preserve empty cells and future move possibilities.
3. Create useful merges.
4. Keep high-value tiles organized.
5. Maximize the chance of eventually reaching 2048.

You MUST choose one of these valid moves:
{valid_moves}

Return only the move name.
Do not return an explanation.

Example output:
left
"""

    response = client.responses.create(
        model="gpt-5.6-luna",
        input=prompt,
    )

    suggestion = response.output_text.strip().lower()

    if suggestion not in valid_moves:
        raise ValueError(
            f"AI returned an invalid move: {suggestion}"
        )

    return suggestion