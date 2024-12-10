import {createRouter, createWebHistory} from 'vue-router'

import main from "@/view/main.vue"

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        // {
        //     path: "/trytomanage",
        //     component: () => import("@/view/trytomanage.vue"),
        // },
        {
            path: "/",
            component: () => import("@/view/main.vue"),
            children: [
                {
                    path: "",
                    component: () => import("@/view/blog/List.vue")
                },
                {
                    path: "post/:id",
                    component: () => import("@/view/blog/ArticleDetail.vue")
                }
            ]
        },
        // {
        //     path: "/post",
        //     component
        // }
    ],
})

export default router
