<template>
  <div>
    <h3>당신에게 추천하는 영화는...</h3>
    <div class="card-container">
      <div v-for="movie in store.movies" :key="movie.id" class="col">
        <MovieCard :movie="movie" />
      </div>
    </div>
    <div class="btn-area">
      <button
        class="btn d-flex"
        @click="getRecommendMovies(store.storedParams)"
      >
        <img class="icon" src="@/assets/movie-repeat.svg" alt="repeat-icon" />
        <div class="btn-text">다른 영화도 보여주세요</div>
      </button>
      <button class="btn d-flex" @click="rewriteRecommend">
        <img
          class="icon"
          src="@/assets/recommend-rewrite.svg"
          alt="rewrite-icon"
        />
        <div class="btn-text">취향을 다시 입력할래요</div>
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieCard from "@/components/movies/MovieCard.vue";
import router from "@/router";

const store = useMovieStore();
const { getRecommendMovies } = store;

onMounted(() => {
  getRecommendMovies();
});

const rewriteRecommend = () => {
  store.resetParams();
  router.push("/");
};
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

.icon {
  width: 40px;
}
.btn-text {
  font-size: 20px;
  margin-left: 10px;
}

.card-container {
  display: flex;
  justify-content: space-around;
  gap: 10px;

  flex-wrap: wrap;

  margin: 10px;
  margin-top: 40px;
  padding: 10px;
}

.col {
  height: max(300px, 25vw);
  cursor: pointer;
}

.btn-area {
  margin-top: 60px;

  display: flex;
  flex-direction: column;
  align-items: center;
}

.btn:hover {
  background-color: #424242;
  border: 1px solid white;
}
</style>
