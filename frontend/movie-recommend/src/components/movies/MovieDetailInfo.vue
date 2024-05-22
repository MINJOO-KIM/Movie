<template>
  <div class="outer">
  <div class="movie-detail-container">
    <div class="movie-poster">
      <RouterLink
      :to="{ name: 'HomeView' }"
      >
        <img class="back-btn" src="@/assets/arrow-left-circle.svg" alt="">
      </RouterLink>
      <img
        class="poster-img"
        :src="`https://image.tmdb.org/t/p/w200${props.movie.posterUrl}`"
        alt="poster-img"
      />
    </div>

    <div class="info-container">
      <h1 class="movie-title">{{ props.movie.title }}</h1>
      <div class="movie-info movie-genres">
          <div v-for="genre in props.movie.genres" :key="genre.name" class="movie-genre">
              {{ genre }}
          </div>
      </div>
      <div class="movie-info">
        <div class="movie-directors">
          감독:<div v-for="director in props.movie.directors" :key="director.name" class="movie-director">
          {{ director }}
          </div>
        </div>

        <div class="movie-actors">
          출연:
          <div v-for="actor in props.movie.actors" :key="actor.name" class="movie-actor">
            {{ actor }},
          </div>
        </div>

        <p><strong>평점:</strong> {{ movie.rating }}</p>
      </div>
      <div>
        <p><strong>줄거리:</strong> {{ movie.overview }}</p>
        <div class="platform-box">
          <div class="movie-platforms">
            <div v-for="platform in props.movie.platforms" :key="platform.name" class="movie-platform">
              <a :href="getPlatformUrl(platform)" target="_blank" rel="">
                <img :src="getPlatformImage(platform)" alt="" />
              </a>
            </div>
          </div>

          <RouterLink :to="{ name: 'OTTHomeView' }">
            <button class="ott-btn">OTT 계정이 없으신가요?</button>
          </RouterLink>
        </div>
      </div>
    </div>
  </div>

  <div class="detail-background">
  </div>
</div>
</template>

<script setup>
import axios from "axios";
import { onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";
import MovieCard from "@/components/movies/MovieCard.vue";

import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";

const store = useMovieStore();
const { movies, getRecommendMovies } = store;

// onMounted(() => {
//   getRecommendMovies();
// });

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
});

function getPlatformUrl(platformName) {
  platformName = platformName.toLowerCase()
  switch (platformName) {
    case "netflix":
      return "https://www.netflix.com/";
    case "watcha":
      return "https://www.watcha.com/";
    case "disneyplus":
      return "https://www.disneyplus.com/";
  }
}

function getPlatformImage(platformName) {
  switch (platformName.toLowerCase()) {
    case "disneyplus":
      return disneyplusImage;
    case "netflix":
      return netflixImage;
    case "watcha":
      return watchaImage;
  }
}
console.log(props.movie.platforms);
</script>

<style scoped>
button {
  color: black;
}

.movie-detail-container {
  display: flex;
  align-items: center;
  gap: 48px;
}

.movie-directors,
.movie-actors,
.movie-genres,
.movie-platforms,
.platform-box {
  display: flex;
  flex-wrap: wrap;
}

.movie-poster {
  display: flex;
  flex-direction: column;
}

.movie-director,
.movie-actor {
  margin-left: 10px;
}

.movie-genre {
  border: 1px solid white;
  border-radius: 50px;

  box-sizing: content-box;
  width: 100px;
  height: 30px;

  background-color: black;
  margin-right: 10px;
  margin-bottom: 10px;

  display: flex;
  justify-content: center;
  align-items: center;
}

.info-container {
  display: flex;
  flex-direction: column;
  gap: 15px;


  max-height: 500px;

  overflow: auto;
}

.info-container::-webkit-scrollbar {
    width: 40px; /* 스크롤바의 너비 */
}

.info-container::-webkit-scrollbar-thumb {
    height: 75%; /* 스크롤바의 길이 */
    background: #595959; /* 스크롤바의 색상 */
    background-clip: padding-box;
    border: 17px solid #171717;
    border-radius: 50px;
}

.info-container::-webkit-scrollbar-track {
    background: #171717; /*스크롤바 뒷 배경 색상*/
}

.movie-platforms {
  gap: 10px;
}


.movie-platform:hover {
  border: 2px solid white;
  border-radius: 20px;
}

.ott-btn {
  color: white;
  background-color: black;

  width: 200px;
  height: 50px;

  border: 1px solid white;
  margin-left: 28px;

  border-radius: 20px;
}

.ott-btn:hover {
  transition: 0.3s;
  background-color: #474747;
}

.outer {
  width: 100vw;
  height: 100vh;
  background-color: #171717;

  position: fixed;

  display: flex;
  justify-content: center;
  align-items: center;

  padding-left: 15vw;
  padding-right: 15vw;
}

.back-btn {
  margin-bottom: 47px;
  width: 60px;
}
</style>
