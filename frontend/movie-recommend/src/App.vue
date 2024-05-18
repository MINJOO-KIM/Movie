<script setup>
import { RouterLink, RouterView } from "vue-router";
import MovieNavbar from "@/components/common/MovieNavbar.vue";
</script>

<template>
  <MovieNavbar />
  <div class="background">
    <RouterView />
  </div>
</template>

<style scoped>
.background {
  width: 100vw;
  height: 100vh;
  background-color: black;
}
</style>
