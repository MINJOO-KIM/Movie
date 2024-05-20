<script setup>
import { RouterLink, RouterView, useRoute} from "vue-router";
import MovieNavbar from "@/components/common/MovieNavbar.vue";
import OTTNavbar from "@/components/common/OTTNavbar.vue";

const route = useRoute();
</script>

<template>
  <!-- route 에 따라 Navbar 변경되는 분기 처리 필요 -->
  <MovieNavbar v-if="route.name === 'Home' || route.name === 'MovieDetailView' || route.name === 'AIRecommendView'"/>
  <OTTNavbar v-else/>
  <img class="background-img" 
  src="@/assets/main-img.png" alt="">
  <div class="background">
  </div>
  <div class="content">
    <hr>
    <RouterView/>
  </div>
</template>


<style scoped>
.background {
  background-color: black;
  width: 100vw;
  height: 100vh;

  position: fixed;
  top: 0px;
  z-index: -1;

  opacity:55%;
}

.background-img {
  position: fixed;
  top: 0px;
  width: 100vw;
  height: 100vh;

  z-index: -2;
}


.content {
  margin-top: 56px;
}

</style>
