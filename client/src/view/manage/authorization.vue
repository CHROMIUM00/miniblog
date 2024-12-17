<script setup lang="ts">
import {ref} from 'vue';
import axios from "axios";
import {useRouter} from "vue-router";

const router = useRouter();

const pw = ref({
    password: "",
});

const state = ref(false)

function submit() {
    axios.post("http://localhost:5000/api/auth/login", pw.value)
        .then(res => {
            console.log(res.data)
            if (res.data.status === "success") {
                router.go(-1)
            } else {
                state.value = true;
            }
        })
}
</script>

<template>
    <div style="display: flex; justify-content: center">

        <div class="box">
            <el-input v-model="pw.password"/>
            <el-button @click="submit">submit</el-button>
        </div>
    </div>
    <div class="mes" v-if="state">AUTHORIZATION FAIL</div>
</template>

<style scoped>
.box {


    width: 400px;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;

    .el-input {
        margin-right: 1em;
    }
}

.mes {
    position: absolute;
    width: 400px;
    display: flex;
    justify-content: center;
    left: calc(100vw / 2 - 200px);
    top: 40vh;
}
</style>
