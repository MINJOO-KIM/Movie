<template>
  <div>
    <!-- bestMovie를 이미 입력했을 때 -->
    <MovieRecommend
      v-if="store.storedParams.bestMovie && store.storedParams.submitted"
    />
    <!-- bestMovie를 아직 입력하지 않았을 때 -->
    <Recommend v-else />
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import MovieRecommend from "@/components/movies/MovieRecommend.vue";
import Recommend from "@/components/movies/Recommend.vue";

const store = useMovieStore();
</script>

<style lang="scss" scoped></style>
