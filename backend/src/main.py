import json
import uuid

from fastapi import FastAPI, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi_socketio import SocketManager
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles

from game import Player, TicTacToeGame

UID_COOKIE_NAME = "ttt_uid"

app = FastAPI()
socket_manager = SocketManager(app=app)

app.mount("/assets", StaticFiles(directory="../../frontend/dist/assets"), name="static")
templates = Jinja2Templates(directory="../../frontend/dist")


@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request) -> Response:
    uid = request.cookies.get(UID_COOKIE_NAME) or str(uuid.uuid4())

    response = templates.TemplateResponse("index.html", {"request": request})
    if UID_COOKIE_NAME not in request.cookies:
        response.set_cookie(key=UID_COOKIE_NAME, value=uid)

    return response


@socket_manager.on("game:new")
async def handle_new_game(sid: str) -> None:
    game = TicTacToeGame.new_game()
    await socket_manager.emit("game:new:callback", json.dumps(game.board))


@socket_manager.on("player:join")
async def handle_join(sid: str, user_cookie: str) -> None:
    player = Player(uid=user_cookie, mark="")
    game = TicTacToeGame()
    game.join_player(player)

    joined_info = {"board": game.board, "player": player.to_dict(), "winner": game.check_winner()}
    await socket_manager.emit("player:join:callback", json.dumps(joined_info), room=sid)


@socket_manager.on("player:mark")
async def handle_mark(sid: str, raw_request: str) -> None:
    uid, mark_index = raw_request.split("|")
    if not mark_index.isdigit() and int(mark_index) > 9:
        return

    game = TicTacToeGame()

    if uid in game.players:
        player = game.players[uid]
    else:
        player = Player(uid=uid, mark="")
        game.join_player(player)

    game.put_mark_of_player(player, int(mark_index))
    winner = game.check_winner()
    if winner != "":
        await socket_manager.emit("game:win", winner)

    await socket_manager.emit("player:mark:callback", json.dumps(game.board))
