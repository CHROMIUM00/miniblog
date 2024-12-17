<script setup lang="ts">
import {onBeforeMount, ref} from "vue";
import axios from "axios";
import {useRoute, useRouter} from "vue-router";
import {ElNotification} from "element-plus";
import {ElMessage} from "element-plus";

const route = useRoute();
const router = useRouter();

const article = ref();

function getPostDetail() {
    axios.get("http://localhost:5000/api/post/getdetail/" + route.params.id)
        .then(res => {
            article.value = res.data.post;
        }).catch(err => {
        console.log(err)
    })
}

function submit() {
    axios.post("http://localhost:5000/api/post/update/" + route.params.id, article.value)
        .then(res => {
            console.log(res.data)
            setTimeout(() => {
                router.push({path: '/admin'})
            }, 3000)
        })
}

onBeforeMount(() => {
    getPostDetail();
})


</script>

<template>
    <div v-if="article">
        <!--        <v-md-editor v-model="article.body" height="80vh"></v-md-editor>-->

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
                <el-input type="textarea" placeholder="简介，留空以自动生成（还没做）"
                          :rows="3" v-model="article.desc"/>
            </el-form-item>
            <el-form-item>
                <v-md-editor height="75vh" v-model="article.body"></v-md-editor>
            </el-form-item>
            <el-form-item>
                <el-button @click="submit">提交</el-button>
            </el-form-item>
        </el-form>
    </div>
</template>

<style scoped>

</style>
