<template>
  <div>
    <h3>당신에게 추천하는 영화는...</h3>
    <div v-for="movie in movies" :key="movie.id" class="col">
        <MovieCard :movie="movie" />
    </div>
  </div>
</template>

<script setup></script>

<style lang="scss" scoped></style>
