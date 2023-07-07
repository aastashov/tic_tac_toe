<template>
  <i class="bi" :class="iconClass"></i>
</template>

<script lang="ts" setup>
import {onMounted, ref} from "vue";

const props = defineProps(["mark"])

const iconClass = ref('');

onMounted(() => {
    if (props.mark === 'x') {
        iconClass.value = 'bi-x-lg'
    } else if (props.mark === 'o') {
        iconClass.value = 'bi-circle'
    } else {
        iconClass.value = ''
    }
});

</script>
