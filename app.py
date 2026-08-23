import streamlit as st

from game2048.board import create_board
from game2048.game import play_move, get_game_status
from game2048.ai import suggest_move


st.set_page_config(
    page_title="2048",
    page_icon="🎮",
    layout="centered",
)


DIRECTION_ICONS = {
    "left": "←",
    "right": "→",
    "up": "↑",
    "down": "↓",
}


def update_suggestion():
    if get_game_status(st.session_state.board) == "playing":
        st.session_state.suggestion = suggest_move(
            st.session_state.board
        )
    else:
        st.session_state.suggestion = None


def new_game():
    st.session_state.board = create_board()
    update_suggestion()


def make_move(direction):
    if get_game_status(st.session_state.board) != "playing":
        return

    st.session_state.board = play_move(
        st.session_state.board,
        direction,
    )

    update_suggestion()


def play_ai_move():
    if get_game_status(st.session_state.board) != "playing":
        return

    direction = st.session_state.suggestion

    if direction is None:
        return

    st.session_state.board = play_move(
        st.session_state.board,
        direction,
    )

    update_suggestion()


if "board" not in st.session_state:
    new_game()


st.title("2048")
st.caption("2048 game engine with AI move suggestions")

board = st.session_state.board
status = get_game_status(board)


# -------------------------
# Board
# -------------------------

for row in board:
    columns = st.columns(4)

    for column, value in zip(columns, row):
        column.markdown(
            f"""
            <div style="
                height: 90px;
                display: flex;
                align-items: center;
                justify-content: center;
                border: 2px solid #888;
                border-radius: 8px;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 8px;
            ">
                {value if value is not None else ""}
            </div>
            """,
            unsafe_allow_html=True,
        )


st.write("")


# -------------------------
# Manual movement controls
# -------------------------

_, up, _ = st.columns(3)

up.button(
    "⬆️",
    width="stretch",
    on_click=make_move,
    args=("up",),
    shortcut="Up",
)

left, down, right = st.columns(3)

left.button(
    "⬅️",
    width="stretch",
    on_click=make_move,
    args=("left",),
    shortcut="Left",
)

down.button(
    "⬇️",
    width="stretch",
    on_click=make_move,
    args=("down",),
    shortcut="Down",
)

right.button(
    "➡️",
    width="stretch",
    on_click=make_move,
    args=("right",),
    shortcut="Right",
)


st.write("")


# -------------------------
# Game status / AI
# -------------------------

if status == "won":
    st.success("🎉 You reached 2048. You win!")

elif status == "lost":
    st.error("💀 No moves available. Game over.")

else:
    st.subheader("🤖 AI Assistant")

    suggestion = st.session_state.suggestion

    if suggestion:
        icon = DIRECTION_ICONS[suggestion]

        st.info(
            f"Recommended move: **{icon} {suggestion.upper()}**"
        )

    st.button(
        "▶ Play AI suggestion",
        on_click=play_ai_move,
        width="stretch",
        shortcut="Space",
        type="primary",
        help="Press Space to play the current AI recommendation",
    )

    st.caption("Press Space to play the recommended move.")

    with st.expander("How does the AI suggestion work?"):
        st.write(
            """
            The AI analyzes the current board and evaluates the
            available moves.

            It then recommends the move that it considers best for
            keeping the game alive and progressing toward 2048.

            **Play AI suggestion** executes one recommended move.

            After the move:
            - the game generates a new tile,
            - the board is updated,
            - and the AI automatically calculates the next recommendation.

            You can also press **Space** instead of clicking the button.
            """
        )


st.write("")


# -------------------------
# New game
# -------------------------

st.button(
    "🔄 New Game",
    on_click=new_game,
    width="stretch",
)