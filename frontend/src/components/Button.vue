<template>
  <button class="game-button" :name="name">
    <PlayerIcon v-if="value" :mark="value"></PlayerIcon>
  </button>
</template>


<script lang="ts" setup>
import PlayerIcon from "@/components/PlayerIcon.vue";

defineProps(['name', 'value'])
</script>

<style>
.game-button {
  background: none;
  border: none;
  width: 100%;
  height: 100%;
  font-size: 50px;
}
</style>
