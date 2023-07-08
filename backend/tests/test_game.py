"""The module to test the TicTacToeGame methods."""
from __future__ import annotations

import pytest
from src.game import TicTacToeGame


@pytest.mark.parametrize(
    "board, winner",
    [
        # Horizontal
        (["x", "x", "x", "", "", "", "", "", ""], "x"),
        (["", "", "", "x", "x", "x", "", "", ""], "x"),
        (["", "", "", "", "", "", "x", "x", "x"], "x"),
        # Vertical
        (["x", "", "", "x", "", "", "x", "", ""], "x"),
        (["", "x", "", "", "x", "", "", "x", ""], "x"),
        (["", "", "x", "", "", "x", "", "", "x"], "x"),
        # Cross
        (["x", "", "", "", "x", "", "", "", "x"], "x"),
        (["", "", "x", "", "x", "", "x", "", ""], "x"),
    ],
)
def test_check_winner(board: list[str], winner: str) -> None:
    """Use this test to check the `check_winner` function."""
    game = TicTacToeGame()
    game.board = board
    assert game.check_winner() == winner
