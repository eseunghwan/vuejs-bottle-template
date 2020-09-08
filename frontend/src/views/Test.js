import Vue from 'vue'
import { router } from "../routes.js";
import config from "../config.js"
import components from "../components";

Vue.config.productionTip = false;
config.register(Vue);
components.register(Vue);

// views
import Test from "./Test.vue";

new Vue({
    render: h => h(Test),
    router
}).$mount("#app")
