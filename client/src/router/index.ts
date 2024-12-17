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
        {
            path: "/admin",
            component: () => import("@/view/manage/manageView.vue"),
            children: [
                {
                    path: "",
                    component: () => import("@/view/manage/postTable.vue")
                },
                {
                    path: "create",
                    component: () => import("@/view/manage/createArticle.vue")
                },
                {
                    path: "update/:id",
                    component: () => import("@/view/manage/updateArticle.vue")
                }
            ]
        }
        // {
        //     path: "/post",
        //     component
        // }
    ],
})

export default router
