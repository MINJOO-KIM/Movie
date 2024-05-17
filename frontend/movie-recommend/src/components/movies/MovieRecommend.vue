<template>
  <div>
    <h3>당신에게 추천하는 영화는...</h3>
    <div v-for="movie in store.movies" :key="movie.id" class="col">
      <MovieCard :movie="movie" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieCard from "@/components/movies/MovieCard.vue";

const store = useMovieStore();
</script>

<style lang="scss" scoped></style>
