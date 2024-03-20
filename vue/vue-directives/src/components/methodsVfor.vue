<script setup>
let triggerAlert = (index) => {
    alert(`${index} has been clicked`)
}
</script>

<template>
    <div>
        <ul>
            <li v-for="index in 5" :key="index">
                <button @click="triggerAlert(index)">Trigger {{ index }}</button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
button {
    margin: 10px;
}
</style>