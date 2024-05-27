<template>
  <div class="outer">
    <div v-if="isLoading" class="loading">
      <h3>당신이 좋아할 만한 영화를 찾고 있어요...</h3>
      <div class="main">
        <div class="loading_circle"></div>
      </div>
    </div>
    <div v-else>
      <div class="card-container" v-if="movies.length > 0">
        <div v-for="movie in movies" :key="movie.id" class="col">
          <MovieCard :movie="movie" />
        </div>
      </div>
      <div v-else>
        <h3 style="margin-top:460px">어떤 영화를 추천해드릴까요?</h3>
      </div>
    </div>

    <form @submit.prevent="getRecommendMoviesByAI()">
      <input type="text" v-model="query">
      <button class="submit-btn">제출</button>
    </form>
  </div>
</template>

<script setup>
import MovieCard from '@/components/movies/MovieCard.vue';
import { onMounted, ref } from 'vue';
import axios from 'axios';


const movies = ref([])
const isLoading = ref(false);
const query = ref('')
const getRecommendMoviesByAI = function() {
  isLoading.value = true;
  const q = query.value;
  query.value = ''
  axios({
    method: 'GET',
    url: 'http://localhost:8000/movies/ai-recommend/',
    params: {
      q
    }
  })
  .then((res) => {
    isLoading.value = false
    query.value = ''
    movies.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}

</script>

<style scoped>
.outer {
  display: flex;
  flex-direction: column;

  align-items: center;
  justify-content: space-between;

  height: 70vh;
}

.loading {
  text-align: center;
  margin-top: 450px;
}

.main{
  width: 90vw;
  margin: 0 auto;
  text-align: center;
}

.loading_circle {
  width: 50px;
  height: 50px;
  margin: 10px auto;
  
  border: 10px solid #e3e3e3;
  border-bottom: 10px solid #000000;
  border-radius: 50%;
  margin-top:30px;
  
  animation: load 1.5s linear infinite;
}

@keyframes load {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

form > input {
  background-color: black;
  border: 1px solid #595959;
  border-radius: 10px;

  width: 500px;
  height: 40px;

  margin-right: 10px;
}
.submit-btn {
  background-color: black;
  
  height: 40px;

  font-size: 16px;
  font-weight: bold;

  border: 1px solid #595959;
  border-radius: 10px;
}

.card-container {
  display: flex;
  justify-content: space-around;
  gap: 10px;

  flex-wrap: wrap;

  margin: 10px;
  margin-top: 150px;
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
