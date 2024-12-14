<script setup lang="ts">
import {onBeforeMount, onMounted, ref} from "vue"
import {useRoute} from "vue-router"
import axios from "axios";
import CommentMaker from "@/view/blog/mainComponent/CommentMaker.vue";
import CommentItem from "@/view/blog/mainComponent/CommentItem.vue";


const route = useRoute();

const postData = ref();
const commentData = ref();

// const postid = Number(route.params.id)

function getPostDetail() {
    axios.get("http://localhost:5000/api/post/getdetail/" + route.params.id)
        .then(res => {
            console.log(res.data)
            postData.value = res.data.post;
            console.log(postData.value)
        }).catch(err => {
        console.log(err)
    })
}

function getComments() {
    axios.get("http://localhost:5000/api/post/getcomment/" + route.params.id)
        .then(res => {
            commentData.value = res.data.comments.map(function (item) {
                return item
            });
            console.log(commentData.value)
        }).catch(err => {
        console.log(err)
    })

}

onBeforeMount(() => {
    getPostDetail();
    getComments();
})

onMounted(() => {
    window.scrollTo(0, 0);
})

</script>

<template>

    <div v-if="postData">

        <div class="title">
            <h1>
                {{ postData.title }}
            </h1>
            <ul>
                <li>{{ postData.created }}</li>
                <li>created by <strong>@{{ postData.author }}</strong></li>
                <li>viewed</li>
            </ul>
        </div>
        <div v-html="postData.body" class="content"></div>

        <hr class="end">
    </div>
    <CommentMaker :postid="route.params.id"/>
    <!--    <commentList />-->
    <!--    <commentList />-->

    <h2>评论</h2>
    <hr>

    <!-- for -->
    <div class="nodata" v-if="!commentData || commentData.length === 0">
        <span>nodata</span>
    </div>
    <div v-for="i in commentData" :key="i.id">

        <CommentItem :author="i.author" :body="i.content" :date="i.created"/>

    </div>
    <!--    <CommentItem :author="'sadwa'" :body="'the quick brown fox jumps over the lazy dog'" :date="'1234/12/12'"/>-->

</template>

<style scoped>
.title {
    h1 {
        border-top: 10px solid #ff6666;
        margin: 0 0 1.5rem 0;
        padding-top: 6rem;
        font-size: 2.5rem;
    }

    ul {
        padding: 0;
        display: flex;
        list-style: none;
        color: #777;

        li {
            padding-right: 2rem;
        }

    }

    margin-bottom: 2rem;
    border-bottom: 1px solid #999;
}

.content :deep(h1) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(h2) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(h3) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(h4) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(h5) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(h6) {
    padding: 1rem 0 0 0;
    text-decoration: underline #ff6666 0.3em;
    text-decoration-skip-ink: none;
}

.content :deep(img) {
    width: 200px;
    object-fit: cover;
}

.end {
    margin: 5rem 0;
    color: #999;
}

.nodata {
    display: flex;

    span {
        color: #999999;
        margin: 3em auto;
    }
}

</style>
