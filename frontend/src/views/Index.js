import Vue from 'vue'
import { router } from "../routes.js";
import config from "../config.js"
import components from "../components";

Vue.config.productionTip = false
config.register(Vue);
components.register(Vue);

// views
import Index from "./Index.vue";

new Vue({
    render: h => h(Index),
    router
}).$mount("#app")
