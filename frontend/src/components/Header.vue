<template>
  <nav class="navbar bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <i class="bi bi-x-lg"></i>
        <i class="bi bi-slash-lg"></i>
        <i class="bi bi-circle"></i>
        <span>Tic Tac Toe</span>
      </a>
      <div>
        Connection {{ state.connected }}.
        <span v-if="playerMark">Your mark: <PlayerIcon :mark="playerMark" /></span>
        <span v-if="store.turn">Turn: <PlayerIcon :mark="store.turn" /></span>
      </div>
      <div>
        <NewGameButton />
      </div>
    </div>
  </nav>
</template>

<script lang="ts" setup>
import {state} from "@/socket";
import PlayerIcon from "@/components/PlayerIcon.vue";
import NewGameButton from "@/components/NewGameButton.vue";
import {store} from "@/utils/store";

defineProps(["playerMark"])

</script>
