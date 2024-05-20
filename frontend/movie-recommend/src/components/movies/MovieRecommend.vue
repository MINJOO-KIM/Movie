<template>
  <div>
    <h3>당신에게 추천하는 영화는...</h3>
    <div v-for="movie in movies" :key="movie.id" class="col">
      <MovieCard :movie="movie" />
    </div>
    <div class="btn-area">
      <button class="btn d-flex">
        <img src="@/assets/movie-repeat.svg" alt="repeat-icon" />
        <div class="btn-text">다른 영화도 보여주세요</div>
      </button>
      <button class="btn d-flex">
        <img src="@/assets/recommend-rewrite.svg" alt="rewrite-icon" />
        <div class="btn-text">취향을 다시 입력할래요</div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieCard from "@/components/movies/MovieCard.vue";

const store = useMovieStore();
const { movies, getRecommendMovies } = store;

onMounted(() => {
  getRecommendMovies();
});
</script>

<style scoped>
button {
  justify-content: center;

  width: 280px;
  border: 1px solid white;
  border-radius: 16px;
  align-items: center;
  margin-bottom: 16px;
}
img {
  /* margin-left: 10px; */
  width: 40px;
}
.btn-text {
  font-size: 20px;
  margin-left: 10px;
}
</style>
