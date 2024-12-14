<script setup lang="ts">
import {ref} from "vue"
import LoginPopover from "@/view/blog/mainComponent/LoginPopover.vue";
import router from "@/router";

console.log("main component online")

// function login() {
//     console.log("trytologin")
// }

const login = ref(false)

function toMain() {
    router.push({path: `/`})
}

</script>

<template>
    <div class="container">

        <div class="aside">
            <img src="@/assets/gww.png" alt="" @click="toMain"/>
            <div class="aside-content">
                <RouterLink to="/" class="links">色彩無盡</RouterLink>
                <RouterLink to="/" class="links">首页</RouterLink>
                <a href="#" class="links">分类</a>
                <p class="links" @click="login = true">登录</p>

            </div>
        </div>

        <div class="main">

            <RouterView/>

        </div>
    </div>

    <!--    <el-dialog v-model="login">-->
    <LoginPopover v-model="login"/>
    <!--    </el-dialog>-->
</template>

<style scoped>
.container {
    --content-width: 800px;
    --sidebar-space: 350px;
    --content-margin: calc((100vw - (var(--content-width) + 2rem)) / 2);
    display: flex;
    flex-flow: column;
    min-height: 100vh;
    /*//background-color: #eee;*/

    .aside {

        position: fixed;
        width: var(--sidebar-space);
        height: 100vh;
        padding-left: calc(var(--content-margin) - var(--sidebar-space) - 2rem);
        display: flex;
        align-items: center;
        align-content: center;

        img {
            cursor: pointer;
        }

        .aside-content {
            height: 100vh;
            align-items: normal;
            display: flex;
            /*flex-direction: column;*/
            writing-mode: vertical-rl;

            .links {
                margin: 1rem;
                color: #000;
                text-decoration: none;
                cursor: pointer;

                &:hover {
                    color: #ff6666;
                    text-decoration: underline 3px;
                }
            }
        }
    }

    .main {
        z-index: 1;
        width: var(--content-width);
        /*//padding-left: var(--content-padding);*/
        /*//padding-right: var(--content-padding);*/
        margin: 0 var(--content-margin);
        padding: 0 1rem;
        background-color: #fff;

        /*//height: 100vh;*/

        hr {
            margin: 2rem 0;
        }
    }
}
</style>
