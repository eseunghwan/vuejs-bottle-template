import Vue from "vue";
import VueRouter from "vue-router";


// views



Vue.use(VueRouter);
export const router = new VueRouter({
    mode: "history",
    routes: [
        // {
        //     path: "/",
        //     component: IndexView
        // },
        // {
        //     path: "/Test",
        //     component: TestView
        // }
    ]
});
