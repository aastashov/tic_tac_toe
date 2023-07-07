<template>
  <button class="btn btn-success" @click="newGameClick">New game</button>
</template>
<script lang="ts" setup>
import {socket} from "@/socket";


function newGameClick() {
    socket.emit("game:new");
}
</script>
