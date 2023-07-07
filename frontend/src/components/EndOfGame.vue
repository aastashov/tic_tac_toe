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
          <NewGameButton></NewGameButton>
        </div>
      </div>
    </div>
  </div>
  <div class="modal-backdrop fade show"></div>
</template>
<script lang="ts" setup>
import {onMounted, ref} from "vue";
import {store} from "@/utils/store";
import NewGameButton from "@/components/NewGameButton.vue";

const modelTitle = ref("");

onMounted(() => {
    if (store.winner === store.player.mark) {
        modelTitle.value = "🎉 You win 🎉"
    } else {
        modelTitle.value = "You lost 😿"
    }
})
</script>
