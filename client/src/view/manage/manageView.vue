<script setup lang="ts">


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
