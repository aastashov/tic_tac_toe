<template>
  <div class="game-board">
    <div class="board-button-item" v-for="(mark, markIndex) in store.board">
      <Button :key="markIndex" :name="markIndex" :value="mark" @click="playerMarkClick(markIndex)"/>
    </div>
  </div>
  <EndOfGame v-if="store.winner !== ''"></EndOfGame>
</template>

<script lang="ts" setup>
import Button from "@/components/Button.vue";
import {socket} from "@/socket";
import {store} from "@/utils/store";
import EndOfGame from "@/components/EndOfGame.vue";


socket.on("game:win", (winnerMark: string) => {
    console.log("game:win", winnerMark);
    store.winner = winnerMark;
})

socket.on('player:mark:callback', (eventJson) => {
    console.log("player:mark:callback", eventJson);
    const parsedEvent = JSON.parse(eventJson);
    store.board = parsedEvent.board;
    store.turn = parsedEvent.turn;
})

function playerMarkClick(markIndex: number) {
    console.log("playerMarkClick", markIndex);
    if (store.turn != store.player.mark) {
        console.log("playerMarkClick: not your turn")
        return
    }

    if (store.board[markIndex] !== store.player.mark) {
        socket.emit("player:mark", `${store.player.uid}|${markIndex}`);
    }
}
</script>


<style>
.game-board {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  background: black;
  gap: 2px;
}

.board-button-item {
  width: 100%;
  height: 200px;
  background: rgba(255, 255, 255, 0.96);
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
