<template>
    <div id="component">
        <label>{{ text }}</label>
    </div>
</template>

<script>
export default {
    props: {
        text: String
    }
}
</script>

<style scoped>
#component > label {
    color: red;
}
</style>
