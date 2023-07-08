"""The nodule to describe a Game."""
from __future__ import annotations

from dataclasses import asdict, dataclass

X_MARK = "x"
O_MARK = "o"


@dataclass(slots=True)
class Player:
    """The player object."""

    uid: str
    mark: str

    def to_dict(self) -> dict[str, str]:
        """Use this function to get a dict representation of Player object."""
        return asdict(self)


class Singleton:
    """
    The simple example of Singleton realisation.

    Examples
    --------
        class SomeClass(Singleton):
            session: ExampleOfSession
            some_data: dict[str, str]

            def __init__(session: ExampleOfSession) -> None:
                # This method will be call every time.
                self.session = session

            def _init(*args, **kwargs) -> None:
                # Called one!
                some_data = {}

        cls1 = SomeClass()
        cls2 = SomeClass()
        assert cls1 is cls2  # Should return True
    """

    def __new__(cls, *args: list[str], **kwargs: dict[str, str]):
        """Use this method to get or create an object."""
        it = cls.__dict__.get("__it__", None)
        if it is not None:
            return it

        cls.__it__ = it = object.__new__(cls)
        it._init(*args, **kwargs)
        return it

    def _init(self, *args: list[str], **kwargs: dict[str, str]) -> None:
        """
        Use this function to first initialization of class.

        If he Singleton object already created, this function was not called.
        """
        pass


class TicTacToeGame(Singleton):
    """The class of Game."""

    board: list[str]
    turn: str
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
        """Use this function to initiate a firs state of Game. It's like __ini__ function."""
        self.board = ["" for _ in range(9)]
        self.turn = ""
        self.players = {}

    @classmethod
    def new_game(cls) -> TicTacToeGame:
        """Use this function to resset a previous game and start a new."""
        new_game = cls()
        new_game.board = ["" for _ in range(9)]
        new_game.turn = ""
        new_game.players = {}
        return new_game

    def to_dict_for_player(self, player: Player) -> dict[str, str | dict[str, str] | list[str]]:
        """Use this function to get a dict representation of Player object."""
        return {"board": self.board, "player": player.to_dict(), "turn": self.turn, "winner": self.check_winner()}

    def join_player(self, uid: str) -> Player | None:
        """
        Use this function to join a Player to game.

        In the TicTacToe game there are only two player.
        :returns: a Player object if the player already in game or can join to game.
        """
        # Choice a mark for the player.
        if uid in self.players:
            return self.players[uid]

        # Join a first user to
        if len(self.players) == 0:
            self.players[uid] = Player(uid=uid, mark=X_MARK)
            self.turn = X_MARK
            return self.players[uid]

        # If in the game already two players we just return.
        if len(self.players) == 2:
            print("room is full")
            return None

        # In this step we know that first player has s X mark.
        self.players[uid] = Player(uid=uid, mark=O_MARK)
        return self.players[uid]

    def takes_turn(self, player: Player, mark_index: int) -> None:
        """
        Use this function to put a mark on the game board.

        When a player takes a turn, his turn is switched to his opponent.
        """
        if self.board[mark_index] == "":
            self.board[mark_index] = player.mark
            self.turn = X_MARK if player.mark != X_MARK else O_MARK

    def check_winner(self) -> str:
        """
        Use this function to check winners. You can call this function everytime.

        :returns: a string with winner mark `x` | `o` or empty string if there is no winner.
        """
        for (c1, c2, c3) in self.winner_cases:
            if self.board[c1] == self.board[c2] == self.board[c3] != "":
                return self.board[c1]
        return ""
