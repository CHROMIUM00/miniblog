<script setup lang="ts">
import {onMounted, ref} from "vue"
import axios from "axios";

import ArticleItem from "@/view/blog/mainComponent/ArticleItem.vue";


const postData = ref();

function getPost() {
    axios.get("http://localhost:5000/api/post/getlist")
        .then(res => {
            // console.log(res.data)
            postData.value = res.data.posts.map(function (item) {
                return item
            })
            console.log(postData.value)
        }).catch(err => {
            console.log(err)
        })
}

onMounted(() => {
    getPost();
})
</script>

<template>
    <div v-for="(i, ind) in postData" :key="ind">
        <!--                {{i.title}}-->
        <ArticleItem :title="i.title" :body="i.desc"
                     :date="i.date" :author="i.author"
                     :id="i.id"/>
        <!--                <infocomment?>-->
        <hr v-if="ind !== postData.length - 1"/>
    </div>
</template>

<style scoped>
hr {
    margin: 2em 0;

    color: #dddddd;
}
</style>
