<template>
  <div class="card h-100">
    <!-- <RouterLink
      :to="{ name: 'MovieDetailView', params: { movie_id: movie.id } }"
    > -->
    <div class="card-body">
      <div>
        <img
          :src="`https://image.tmdb.org/t/p/original/${props.movie.poster_path}`"
          alt="poster-img"
        />
      </div>
    </div>
    <!-- </RouterLink> -->
  </div>
</template>

<script setup>
const props = defineProps({
  movie: {
    type: Object,
    required: true,
  },
});
// console.log(props.movie);
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
