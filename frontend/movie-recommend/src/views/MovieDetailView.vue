<template>
  <div v-if="movie" class="movie-detail-container">
    <MovieDetailInfo :movie="movie" />
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import { useRoute } from "vue-router";
import MovieDetailInfo from "@/components/movies/MovieDetailInfo.vue";

// const store = useMovieStore();
// const { movies, getRecommendMovies } = store;
const route = useRoute();
const moviePk = route.params.movie_id;

const movie = ref({});

const API_URL = "http://127.0.0.1:8000";
const fetchMovieDetail = (moviePk) => {
  axios({
    method: "GET",
    url: `${API_URL}/movies/${moviePk}`,
  })
    .then((res) => {
      console.log(res);
      movie.value = res.data;
    })
    .catch((err) => console.log(err));
};
onMounted(() => {
  fetchMovieDetail(moviePk);
});
</script>

<style scoped>
.movie-detail-container {
  display: flex;
  align-items: center;
  height: 90vh;
}
</style>