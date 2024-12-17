<script setup lang="ts">
import {ref} from "vue"
import axios from "axios";
import {useRouter} from "vue-router";

const router = useRouter();

const article = ref({
    title: "",
    author: "CHROMIUM00",
    body: "",
    desc: "",
})

function submit() {
    axios.post("http://localhost:5000/api/post/create", article.value)
        .then(res => {
            console.log(res.data)
            router.push({path: '/admin'})
        })
}

</script>

<template>
    <el-form :model="article" :label-position="'top'">
        <el-row :gutter="20">
            <el-col :span="12">
                <el-form-item label="Title">
                    <el-input v-model="article.title"/>
                </el-form-item>
            </el-col>
            <el-col :span="12">
                <el-form-item label="Author">
                    <el-input v-model="article.author" placeholder="CHROMIUM00"/>
                </el-form-item>
            </el-col>
        </el-row>
        <el-form-item prop="body">
            <el-input type="textarea" placeholder="简介，留空以自动生成（还没做）" :rows="3" v-model="article.desc"/>
        </el-form-item>
        <el-form-item>
            <v-md-editor height="75vh" v-model="article.body"></v-md-editor>
        </el-form-item>
        <el-form-item>
            <el-button @click="submit">提交</el-button>
        </el-form-item>
    </el-form>
</template>

<style scoped>
/*.el-row {*/
/*    margin: 1em 0;*/
/*}*/
</style>
