<template>
  <div class="movie-detail-container">
    <div class="movie-poster">
      <img
        class=""
        :src="`https://image.tmdb.org/t/p/w200${props.movie.posterUrl}`"
        alt="poster-img"
      />
    </div>
    <h1 class="movie-title">{{ props.movie.title }}</h1>
    <p class="movie-title">장르:</p>
    <div class="movie-info">
      <ul class="genre-list">
        <li v-for="genre in props.movie.genres" :key="genre.name">
          <div>
            {{ genre }}
          </div>
        </li>
      </ul>
    </div>
    <div class="movie-info">
      <div class="movie-directors">감독:</div>
      <div v-for="director in props.movie.directors" :key="director.name">
        {{ director }}
      </div>
      <p class="movie-actors">출연:</p>
      <div class="actors-list">
        <li v-for="actor in props.movie.actors" :key="actor.name">
          {{ actor }}
        </li>
      </div>
      <p><strong>평점:</strong> {{ movie.rating }}</p>
      <p><strong>줄거리:</strong> {{ movie.overview }}</p>
    </div>
  </div>
</template>

<script setup>
const store = useMovieStore();
const { movies, getRecommendMovies } = store;

onMounted(() => {
  getRecommendMovies();
});

const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
});
</script>

<style scoped>
button {
  color: black;
}
</style>
