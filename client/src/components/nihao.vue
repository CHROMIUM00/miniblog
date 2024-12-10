<script setup lang="ts">
import {ref} from 'vue'
import axios from "axios";

const msg = ref("nihao")
axios.get("http://localhost:5000/api/test")
    .then(res => {msg.value = res.data})
</script>

<template>
    {{msg}}
</template>

<style scoped>

</style>
