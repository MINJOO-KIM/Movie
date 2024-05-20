<template>
  <div>
    <MovieRecommend />
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieRecommend from "@/components/movies/MovieRecommend.vue";

const store = useMovieStore();

onMounted(() => {
  store.getRecommendMovies();
});
</script>

<style lang="scss" scoped></style>
