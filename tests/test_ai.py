from game2048.ai import suggest_move
import game2048.ai as ai
from types import SimpleNamespace


def test_ai_suggests_a_valid_move(monkeypatch):
    board = [
        [None, 2, None, None],
        [None, None, None, None],
        [None, None, None, None],
        [None, None, None, None],
    ]

    monkeypatch.setenv("OPENAI_API_KEY", "test-key")

    response = SimpleNamespace(output_text="left")
    client = SimpleNamespace(
        responses=SimpleNamespace(
            create=lambda **kwargs: response
        )
    )

    monkeypatch.setattr(ai, "OpenAI", lambda api_key: client)

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

DEEPSEEK_API_KEY = "your_key_here"

def suggest_move_with_remote_ai(board):
    if not DEEPSEEK_API_KEY:
        raise ValueError("DeepSeek API key is not configured")

    client = OpenAI(
        api_key=DEEPSEEK_API_KEY,
        base_url="https://api.deepseek.com",
    )

    prompt = f"""
    You are playing a 4x4 game of 2048.
    Current board:
    {board}
    Choose the best next move to maximize the chance of reaching 2048
    and avoid game over.
    Valid answers are only:
    left
    right
    up
    down
    Return exactly one word and nothing else.
    """
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {
                "role": "system",
                "content": "You are an expert 2048 player.",
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0,
    )
    suggestion = response.choices[0].message.content.strip().lower()
    valid_moves = ["left", "right", "up", "down"]
    if suggestion not in valid_moves:
        return None
    return suggestion
