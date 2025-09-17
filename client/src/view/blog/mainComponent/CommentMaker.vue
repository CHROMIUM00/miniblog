<script setup lang="ts">


import {reactive, ref} from "vue";
import axios from "axios";
import {useRouter} from "vue-router";

const router = useRouter()

const props = defineProps({
    post_id: String,
    post_title: String,
})

const commentItem = ref({
    author: "",
    mail: "",
    body: "",
    post_title: props.post_title,
})

function submit() {
    if (commentItem.value.author === "") {
        commentItem.value.author = "Anonymous"
    }

    axios.post("http://localhost:5000/api/post/addcomment/" + props.post_id, commentItem.value)
        .then(res => {
            console.log(res.data)
            router.go(0)
        })
}
</script>

<template>
    <div class="comment-maker">
        <el-form :model="commentItem" :label-position="'top'">
            <el-row :gutter="20">

                <el-col :span="12">

                    <el-form-item label="昵称">
                        <el-input placeholder="Anonymous" v-model="commentItem.author"/>
                    </el-form-item>
                </el-col>
                <el-col :span="12">

                    <el-form-item label="邮箱">
                        <el-input v-model="commentItem.mail" placeholder="填写邮箱可能收到回复"/>
                    </el-form-item>
                </el-col>
            </el-row>
            <el-form-item prop="body">
                <el-input type="textarea" placeholder="在这里留言" :rows="5" v-model="commentItem.body" prop="body"/>
            </el-form-item>
            <el-form-item>
                <el-button @click="submit" v-if="commentItem.body !== ''">提交</el-button>
                <el-button disabled v-else>提交</el-button>
            </el-form-item>
        </el-form>
    </div>


</template>

<style scoped>
.comment-maker {
    margin: 5rem 0;
}
</style>
