"""The module to describe web server and socker server for Game."""
from __future__ import annotations

import json
import uuid

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi_socketio import SocketManager
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from game import TicTacToeGame

UID_COOKIE_NAME = "ttt_uid"

app = FastAPI()
socket_manager = SocketManager(app=app)

app.mount("/assets", StaticFiles(directory="../../frontend/dist/assets"), name="static")
templates = Jinja2Templates(directory="../../frontend/dist")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> Response:
    """Use this function to return a main page of Game."""
    uid = request.cookies.get(UID_COOKIE_NAME) or str(uuid.uuid4())

    response = templates.TemplateResponse("index.html", {"request": request})
    if UID_COOKIE_NAME not in request.cookies:
        response.set_cookie(key=UID_COOKIE_NAME, value=uid)

    return response


@socket_manager.on("game:new")
async def handle_new_game(_: str) -> None:
    """
    Use this function to receive and handle the `game:new` socket event.

    The new_game handler reset the current game and returns new game for players.
    """
    game = TicTacToeGame.new_game()
    await socket_manager.emit("game:new:callback", json.dumps({"board": game.board, "turn": game.turn}))


@socket_manager.on("player:join")
async def handle_join(sid: str, player_cookie: str) -> None:
    """
    Use this function to receive and handle the `player:join` socket event.

    The join handler get a player_cookie to join to game. If the room is full, the player
     receive the `player:join:room:full` event.
    """
    game = TicTacToeGame()

    player = game.join_player(player_cookie)
    if player is None:
        await socket_manager.emit("player:join:room:full", room=sid)
        return

    await socket_manager.emit("player:join:callback", json.dumps(game.to_dict_for_player(player)), room=sid)


@socket_manager.on("player:mark")
async def handle_mark(sid: str, raw_request: str) -> None:
    """
    Use this function to receive and handle the `player:mark` socket event.

    The mark handler get a custom request from player like `{uid}|{index_of_cell_on_board}`, parse this request, and
     takes a turn if the player joined to the Game. The player cannot override any cell with a value. If a player's
      turn wins the game, all players receive a `game:win' event with the winner's mark.
    """
    uid, mark_index = raw_request.split("|")
    if not mark_index.isdigit() and int(mark_index) > 9:
        return

    game = TicTacToeGame()
    player = game.join_player(uid)
    if player is None:
        await socket_manager.emit("player:join:room:full", room=sid)
        return

    game.takes_turn(player, int(mark_index))
    winner = game.check_winner()
    if winner != "":
        await socket_manager.emit("game:win", winner)

    await socket_manager.emit("player:mark:callback", json.dumps({"board": game.board, "turn": game.turn}))
