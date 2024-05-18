<template>
  <div>
    <p>HomeView</p>
    <MovieRecommend />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieRecommend from "@/components/movies/MovieRecommend.vue";

const store = useMovieStore();

onMounted(() => {
  store.getMovies();
});
</script>

<style lang="scss" scoped></style>
