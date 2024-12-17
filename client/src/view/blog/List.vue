<script setup lang="ts">
import {onMounted, ref} from "vue"
import axios from "axios";

import ArticleItem from "@/view/blog/mainComponent/ArticleItem.vue";
import CommentItem from "@/view/blog/mainComponent/CommentItem.vue";


const listData = ref();

function getList() {
    axios.get("http://localhost:5000/api/post/getlist")
        .then(res => {
            listData.value = res.data.data;
        })
}

onMounted(() => {
    getList();
})
</script>

<template>
    <div v-for="(i, ind) in listData" :key="ind">
        <!--                {{i.title}}-->
        <ArticleItem v-if="i.type == 'article'" :title="i.title" :body="i.desc"
                     :date="i.created" :author="i.author"
                     :id="i.id"/>
        <!--                <infocomment?>-->
        <CommentItem v-if="i.type == 'comment'" :author="i.author" :body="i.content"
                     :date="i.created" :to="i.post_title"/>
        <hr v-if="ind !== listData.length - 1"/>
    </div>
</template>

<style scoped>
hr {
    margin: 2em 0;

    color: #dddddd;
}
</style>
