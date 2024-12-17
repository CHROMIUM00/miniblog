<script setup lang="ts">
import {onBeforeMount, ref} from "vue";
import axios from "axios";

import {useRouter} from "vue-router"


const postData = ref();

function getPost() {
    axios.get("http://127.0.0.1:5000/api/post/getpostlist")
        .then(res => {
            postData.value = res.data.data;
        })
}

onBeforeMount(() => {
    getPost()
})

const router = useRouter();

function toUpdatePost(id: Number) {
    router.push({path: 'admin/update/' + id})
}

function toDelete(id: Number) {
    axios.post("http://localhost:5000/api/post/delete/" + id)
        .then(res => {
            console.log(res.data)
        })
}
</script>

<template>
    <el-scrollbar>
        <el-table :data="postData" v-if="postData">
            <el-table-column prop="title" label="Title"/>
            <el-table-column prop="author" label="Author"/>
            <el-table-column prop="desc" label="Description"/>
            <el-table-column prop="created" label="Date"/>
            <el-table-column label="Operation">
                <template #default="scope">
                    <el-button size="small" @click="toUpdatePost(scope.row.id)">Update</el-button>
                    <el-button size="small" type="danger" @click="toDelete(scope.row.id)">Delete</el-button>
                </template>
            </el-table-column>
        </el-table>
    </el-scrollbar>
</template>

<style scoped>

</style>
