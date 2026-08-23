# 2048

A small Python implementation of 2048 with a Streamlit interface and optional AI move suggestions.

## Quick start

Requires Python 3.10 or newer.

### 1. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

### 3. Start the game

```bash
streamlit run app.py
```

The application opens in a browser. Use the arrow buttons or keyboard arrows to move tiles.

## AI suggestions

AI suggestions are optional. Manual moves are handled locally and do not call the remote API.

To enable suggestions, set an OpenAI API key in a local `.env` file:

```text
OPENAI_API_KEY=your_api_key_here
```

Then click **Ask AI for best move** in the application. The key is loaded from the environment and must never be committed to Git.

## Run the tests

```bash
pytest
```

The tests cover board creation, tile generation, all movement directions, merging, and win/loss detection. The AI unit test uses a mocked response, so the test suite does not require network access or an API key.

## Project structure

```text
app.py                 Streamlit UI and user actions
src/game2048/
  board.py             Board creation and random tile generation
  moves.py             Pure left/right/up/down movement logic
  game.py              Move execution, tile generation, and game status
  ai.py                Valid-move calculation and OpenAI suggestion handling
tests/
  test_board.py        Board and tile-generation tests
  test_moves.py        Movement and merge tests
  test_game.py         Game rules and endgame tests
  test_ai.py           AI suggestion tests with a mocked API response
pyproject.toml         Project metadata and dependencies
```

## Controls

- Arrow buttons or keyboard arrows: make a local move
- **Ask AI for best move**: request a recommendation
- **Play AI suggestion** or Space: execute the displayed recommendation
- **New Game**: create a new board
