<script setup lang="ts">

const props = defineProps({
    author: String,
    body: String,
    date: String,
})

</script>

<template>

    <div class="comment-item">
        <p class="name">来自 <strong>@{{ author }}</strong></p>
        <p class="text">{{ body }}</p>
        <p class="date">{{ date }}</p>
    </div>

</template>

<style scoped>

.comment-item{
    border-left: 0.3em solid #ff6666;
    padding-left: 1em;
    margin: 2rem 0;
    .name{
        font-size:0.8em;
        color: #999999;
        strong{
            color: #777777;
        }
    }
    .text {
        word-break: break-word;
    }
    .date{
        font-size: 0.8em;
        color: #999999;
    }
}


</style>
