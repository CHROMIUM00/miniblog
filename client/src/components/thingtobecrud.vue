<script setup lang="ts">
interface Book {
    title: string,
    author: string,
    read: boolean,
}

const foo1 = () => {
    console.log("f1")
}
const foo2 = () => {
    console.log("f2")
}


import {ref, onMounted} from 'vue';
import axios from "axios";

const tableData = ref()

function getBook() {
    axios.get("http://localhost:5000/api/books")
        .then(res => {
            console.log("hi")
            console.log(res.data.books);
            tableData.value = res.data.books;
        })
}

function addBook(payload) {
    axios.post("http://localhost:5000/api/books", payload)
        .then(() => {
            getBook();
        })
}


onMounted(() => {
    getBook();
});


const form = ref({
    title: "",
    author: "",
    read: false,
})
const dialogFormVisible = ref(false)

function onSubmit() {
    // event.preventDefault();
    addBook(form.value);
}

function reset() {
    form.value.title = "";
    form.value.author = "";
    form.value.read = false;
}

</script>

<template>
    nihao

    <el-button type="primary" @click="dialogFormVisible = true">Add book</el-button>

    <div class="container" style="width: 100%">
        <el-table :data="tableData">
            <el-table-column prop="title" label="Title"/>
            <el-table-column prop="author" label="Author"/>
            <el-table-column prop="read" label="Read?"/>
            <el-table-column>
                <template #default="scope">
                    <el-button size="small" @click="foo1">Update</el-button>
                    <el-button size="small" type="danger" @click="foo2">Delete</el-button>
                </template>
            </el-table-column>
        </el-table>

    </div>

    <el-dialog v-model="dialogFormVisible" title="Add Book">
        <el-form :model="form" label-width="auto">
            <el-form-item label="Title">
                <el-input v-model="form.title"/>
            </el-form-item>
            <el-form-item label="Author">
                <el-input v-model="form.author"/>
            </el-form-item>
            <el-form-item label="Read?">
                <el-switch v-model="form.read"/>
            </el-form-item>
        </el-form>
        <template #footer>
            <el-button type="primary" @click="onSubmit">Submit</el-button>
            <el-button type="danger" @click="reset">Reset</el-button>
        </template>
    </el-dialog>

</template>

<style scoped>
el-dialog {
    padding: 100px;
}
</style>
