<template>
  <div class="container-fluid">
    <Header :playerMark="store.player.mark"/>
    <div class="content">
      <GameBoard/>
    </div>
  </div>
</template>

<script lang="ts" setup>
import Header from "@/components/Header.vue";
import GameBoard from "@/components/GameBoard.vue";

import {socket} from "@/socket";
import {onMounted} from "vue";
import {store} from "@/utils/store";

socket.on("game:new:callback", (eventJson: string) => {
    console.log("game:new:callback", eventJson);
    const parsedEvent = JSON.parse(eventJson);
    store.board = parsedEvent.board;
    store.turn = parsedEvent.turn;
    store.winner = "";

    socket.emit("player:join", store.player.uid);
})

socket.on("player:join:callback", (eventJson) => {
    console.log("player:join:callback", eventJson)
    const joinedInfo = JSON.parse(eventJson);
    store.player = joinedInfo.player;
    store.board = joinedInfo.board;
    store.winner = joinedInfo.winner;
    store.turn = joinedInfo.turn;
})

socket.on("connect", () => {
    console.log("connected");
    console.log("store.player.uid", store.player.uid)
    socket.emit("player:join", store.player.uid);
})

onMounted(() => {
    socket.connect();
})
</script>

<style>
.content {
  padding: 40px 20px;
  max-width: 1024px;
  margin: auto;
}
</style>
