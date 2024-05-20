<template>
  <div class="card-content">
    <!-- <RouterLink
      :to="{ name: 'MovieDetailView', params: { movie_id: movieId } }"
    /> -->

    <img
      class=""
      :src="`https://image.tmdb.org/t/p/w500${props.movie.posterUrl}`"
      alt="poster-img"
    />

    <!-- </RouterLink> -->
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
img {
  width: 100%;
  height: 100%;
}

.card-content {
  height: 100%;
  width: max(200px, 18vw);

  box-shadow: 0 14px 28px rgba(0, 0, 0, 0.25), 0 10px 10px rgba(0, 0, 0, 0.22);
}
</style>
