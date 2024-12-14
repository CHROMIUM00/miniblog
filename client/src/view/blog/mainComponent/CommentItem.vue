<script setup lang="ts">

const props = defineProps({
    author: String,
    body: String,
    date: String,
    to: String,
})

</script>

<template>

    <div class="comment">
        <div class="to" v-if="to != null">
            <p>文章 <strong>{{ to }}</strong> 的评论</p>
        </div>
        <div class="comment-item">
            <p class="name">来自 <strong>@{{ author }}</strong></p>
            <p class="text">{{ body }}</p>
            <p class="date">{{ date }}</p>
        </div>
    </div>

</template>

<style scoped>

.comment {
    margin: 2rem 0;

    .to {
        font-size: 0.8em;
        color: #999999;
    }

    .comment-item {
        border-left: 0.3em solid #ff6666;
        padding-left: 1em;

        .name {
            font-size: 0.8em;
            color: #999999;

            strong {
                color: #777777;
            }
        }

        .text {
            word-break: break-word;
        }

        .date {
            font-size: 0.8em;
            color: #999999;
        }
    }
}


</style>
