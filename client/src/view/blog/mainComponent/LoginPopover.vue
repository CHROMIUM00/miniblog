<script setup lang="ts">
import {ref} from "vue"
import axios from "axios";

const model = defineModel()

const user = ref({
    username: "",
    password: "",
})

function login() {
    axios.post("http://localhost:5000/api/user/login", user.value)
        .then(res => {
            console.log(res.data)
            if (res.data.code === 200) {
                model.value = false
            }
        })
}

</script>

<template>

    <el-dialog v-model="model" title="登录" width="500">
        <el-form :model="user">
            <el-form-item label="用户名" label-width="70px">
                <el-input v-model="user.username"/>
            </el-form-item>
            <el-form-item label="密码" label-width="70px">
                <el-input v-model="user.password" show-password/>
            </el-form-item>
        </el-form>
        <template #footer>
            <el-button type="primary" @click="login">登录</el-button>
        </template>
    </el-dialog>

</template>

<style scoped>

</style>
