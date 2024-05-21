<template>
    <div class="my-party-container">
        <MyPartyCard/>
    </div>
</template>

<script setup>
import MyPartyCard from '@/components/otts/MyPartyCard.vue';
</script>

<style scoped>

.my-party-container {
    display: flex;
    justify-content: center;
    align-items: center;

    height: 90vh;
    width: 100vw;
}
</style> 