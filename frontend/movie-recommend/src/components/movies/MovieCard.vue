<template>
  <div class="card h-100 d-flex">
    <RouterLink
      :to="{
        name: 'MovieDetailView',
        params: { movie_id: props.movie.movieId },
      }"
    >
      <div class="card-body">
        <div>
          <img
            class=""
            :src="`https://image.tmdb.org/t/p/w200${props.movie.posterUrl}`"
            alt="poster-img"
          />
        </div>
      </div>
    </RouterLink>
  </div>
  <!-- <div class="">
    <div>
      <img
        class=""
        :src="`https://image.tmdb.org/t/p/w200${props.movie.posterUrl}`"
        alt="poster-img"
      />
    </div>
  </div> -->
</template>

<script setup>
const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
});
console.log(props.movie);
</script>

<style scoped>
.card a,
.card a:hover {
  color: inherit;
  text-decoration: none;
}
.card {
  color: black !important;
}
</style>
