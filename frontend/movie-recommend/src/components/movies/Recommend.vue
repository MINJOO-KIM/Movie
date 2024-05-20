<template>
  <div>
    <div class="title">당신의 취향을 알려주세요</div>
    <div class="recommend-input">
      <form @submit.prevent="submitForm">
        <div class="genres">
          <div>선호하는 장르</div>
          <div v-for="genre in genres" :key="genre.id">
            <button
              type="button"
              :class="[
                'genre-btn',
                { selected: selectedGenres.includes(genre.id) },
              ]"
              @click="toggleGenre(genre.id)"
            >
              {{ genre.name }}
            </button>
          </div>
        </div>
        <input type="submit" value="제출" />
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useMovieStore } from "@/stores/movie";

const store = useMovieStore();
const { genres, getGenres } = store;

const gender = ref("");
const age = ref(0);
const bestMovie = ref("");
const selectedGenres = ref([]);
const directors = ref("");
const actors = ref("");

// 장르 선택 토글 함수
const toggleGenre = (genreId) => {
  if (selectedGenres.value.includes(genreId)) {
    selectedGenres.value = selectedGenres.value.filter((id) => id !== genreId);
  } else {
    selectedGenres.value.push(genreId);
  }
};

onMounted(() => {
  getGenres();
});
</script>

<style scoped>
input {
  color: black;
}
.genre-btn {
  background-color: black;
  color: white;
  width: 100px;
  height: 50px;
  border-radius: 2rem;
  margin: 5px;
}
.genre-btn:hover {
  transition: background-color 0.3s;
  background-color: #424242;
  opacity: 85%;
}
.genre-btn.selected {
  background-color: #424242;
  opacity: 85%;
}
</style>
