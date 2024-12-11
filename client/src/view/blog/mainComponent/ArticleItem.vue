<script setup lang="ts">

import {useRouter} from "vue-router";

const router = useRouter()

const props = defineProps({
    author: String,
    body: String,
    date: Date,
    title: String,

    id: Number
})

function toPost() {
    router.push({path: `/post/${props.id}`})
}

</script>

<template>
    <div class="article" @click="toPost()">
        <h1 class="title">{{ title }}</h1>
        <p>{{ body }}</p>
        <!--                <hr>-->
        <ul>
            <li>{{ date }}</li>
            <li>created by {{ author }}</li>
            <li></li>
        </ul>
    </div>
</template>

<style scoped>
.article {
    background-color: #fff;
    margin: 1rem 0;
    padding-bottom: 0.1rem;

    box-shadow: 0 0 0.5rem 0 rgba(0, 0, 0, 0.1);

    .title {
        margin: 0;
        padding: 0.3rem 1.5rem;
        background-color: #f66;
        font-size: 1.5rem;
    }

    p {

        padding: 0 1.5rem;
    }

    ul {
        display: flex;
        list-style: none;
        margin: 1rem 0;
        padding: 0 1.5rem;
        color: #777;

        li {
            padding-right: 2rem;
        }

    }
}
</style>
