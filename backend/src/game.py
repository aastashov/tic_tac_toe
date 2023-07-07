from __future__ import annotations

from dataclasses import dataclass

X = "x"
O = "o"


@dataclass
class Player:
    uid: str
    mark: str

    def to_dict(self) -> dict[str, str]:
        return {"uid": self.uid, "mark": self.mark}


class Singleton:
    def __new__(cls, *args: list[str], **kwargs: dict[str, str]):
        it = cls.__dict__.get("__it__", None)
        if it is not None:
            return it

        cls.__it__ = it = object.__new__(cls)
        it._init(*args, **kwargs)
        return it

    def _init(self, *args: list[str], **kwargs: dict[str, str]) -> None:
        pass


class TicTacToeGame(Singleton):
    board: list[str]
    players: dict[str, Player]

    winner_cases = (
        # Horizontal
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        # Vertical
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        # Cross
        (0, 4, 8),
        (2, 4, 6),
    )

    def _init(self, *args: list[str], **kwargs: dict[str, str]) -> None:
        self.board = ["" for _ in range(9)]
        self.players = {}

    @classmethod
    def new_game(cls) -> TicTacToeGame:
        new_game = cls()
        new_game.board = ["" for _ in range(9)]
        new_game.players = {}
        return new_game

    def join_player(self, player: Player) -> None:
        if player.uid in self.players:
            player.mark = self.players[player.uid].mark
            return

        if len(self.players) == 2:
            print("room is full")
            return

        if len(self.players) == 0:
            player.mark = X
            self.players[player.uid] = player
            return

        if player.uid not in self.players:
            first_player = self.players[list(self.players.keys())[0]]
            player.mark = X if first_player.mark != X else O

        self.players[player.uid] = player

    def put_mark_of_player(self, player: Player, mark_index: int) -> None:
        if self.board[mark_index] == "":
            self.board[mark_index] = player.mark

    def check_winner(self) -> str:
        for (c1, c2, c3) in self.winner_cases:
            if self.board[c1] == self.board[c2] == self.board[c3] != "":
                return self.board[c1]
        return ""
