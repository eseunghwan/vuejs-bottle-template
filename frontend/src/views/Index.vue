<template>
    <div id="app">
        <label-box v-bind:text="lbl1_text"></label-box>
        <button id="btn1" v-on:click="btn1_click">click me!</button>
        <label>Hi!</label>
    </div>
</template>

<script>
import axios from "axios";

export default {
    data: function() {
        return {
            lbl1_text: "hello, vue_bs!"
        }
    },
    methods: {
        btn1_click: function() {
            axios.get(`${this.$fn}/get`).then((res) => {
                var data = res.data;
                this.lbl1_text = data.message;
            }).then(() => {
                axios.post(`${this.$fn}/set`, { message: "post" });
            });
        }
    }
};
</script>

<style>
#app {
    display: flex;
    flex-direction: column;
}
</style>
