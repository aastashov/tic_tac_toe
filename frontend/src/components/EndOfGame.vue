<template>
  <div class="modal fade show" id="staticBackdrop" data-bs-backdrop="static"
       data-bs-keyboard="false" tabindex="-1"
       aria-labelledby="staticBackdropLabel" aria-hidden="true" style="display: block">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h2 class="modal-title w-100 text-center">{{ modelTitle }}</h2>
        </div>
        <div class="modal-body text-center">
          Thank you for playing this game 🤗
        </div>
        <div class="modal-footer">
          <NewGameButton />
        </div>
      </div>
    </div>
  </div>
  <div class="modal-backdrop fade show"></div>
</template>
<script lang="ts" setup>
import {computed} from "vue";
import {store} from "@/utils/store";
import NewGameButton from "@/components/NewGameButton.vue";

const modelTitle = computed(() => store.winner === store.player.mark ? "🎉 You win 🎉" : "You lost 😿");
</script>
