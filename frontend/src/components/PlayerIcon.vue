<template>
  <i class="bi" :class="iconClass"></i>
</template>

<script lang="ts" setup>
import {computed} from "vue";

const markMap: { [key: string]: string } = {
    "x": "bi-x-lg",
    "o": "bi-circle",
}

const props = defineProps(["mark"]);
const iconClass = computed(() => markMap[props.mark] || "");
</script>
