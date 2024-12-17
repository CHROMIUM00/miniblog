<script setup lang="ts">
import {onBeforeMount, onMounted} from "vue";
import {check} from "./auth.ts"
import axios from "axios";
import {useRouter} from "vue-router";

const router = useRouter();

onMounted(() => {
    console.log("hi")
    axios.get("http://localhost:5000/api/auth/state")
        .then(res => {
            console.log(res.data)
            if (res.data.logged === "false") {
                router.push({path: "/authorization"})
            }
        })
})
</script>

<template>
    <div class="common-layout">
        <el-container>
            <el-aside width="200px">
                <el-menu :router="true">
                    <el-menu-item index="/admin">
                        Article list
                    </el-menu-item>
                    <el-menu-item index="/admin/create">
                        Create new article
                    </el-menu-item>
                </el-menu>
            </el-aside>
            <el-container>
                <el-main>
                    <RouterView/>
                    <!--                    <v-md-editor></v-md-editor>-->
                </el-main>
            </el-container>
        </el-container>
    </div>
</template>

<style scoped>
.el-menu {
    height: 100vh;
}

</style>
