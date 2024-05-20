<template>
  <div>
    <div class="title">당신의 취향을 알려주세요</div>
    <div class="recommend-input">
      <form @submit.prevent="submitForm">
        <div class="gender">
          <div>성별</div>
          <button
            type="button"
            :class="['gender-btn', { selected: gender === 'male' }]"
            @click="selectGender('male')"
          >
            남
          </button>
          <button
            type="button"
            :class="['gender-btn', { selected: gender === 'female' }]"
            @click="selectGender('female')"
          >
            여
          </button>
        </div>
        <div class="age">
          <label for="age">나이</label>
          <div class="age-input-container">
            <input type="number" id="age" name="age" v-model="age" min="0" />
          </div>
        </div>
        <div class="best-movie">
          <label for="best-movie">최근에 재미있게 본 영화</label>
          <input type="text" id="best-movie" v-model="bestMovie" />
        </div>
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
        <div class="directors">
          <label for="directors">선호하는 감독</label>
          <input type="text" id="directors" v-model="directors" />
        </div>
        <div class="actors">
          <label for="actors">선호하는 배우</label>
          <input type="text" id="actors" v-model="actors" />
        </div>
        <br /><br />
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

// 성별 선택 함수
const selectGender = (selectedGender) => {
  gender.value = selectedGender;
};

// 장르 선택 토글 함수
const toggleGenre = (genreId) => {
  if (selectedGenres.value.includes(genreId)) {
    selectedGenres.value = selectedGenres.value.filter((id) => id !== genreId);
  } else {
    selectedGenres.value.push(genreId);
  }
};

// 폼 제출 핸들러 함수
const submitForm = () => {
  const formData = {
    bestMovie: bestMovie.value,
    selectedGenres: selectedGenres.value,
    directors: directors.value,
    actors: actors.value,
  };
  console.log("Form Data: ", formData);

  const API_URL = "http://127.0.0.1:8000";

  axios({
    method: "GET",
    url: `${API_URL}/movies/recommend`,
    params: {
      "best-movie": bestMovie.value,
      genres: selectedGenres.value,
      directors: directors.value,
      actors: actors.value,
    },
  })
    .then((res) => {
      console.log(res);
    })
    .catch((err) => {
      console.log(err);
    });
};

onMounted(() => {
  getGenres();
});
</script>

<style scoped>
input {
  color: black;
}
.genre-btn,
.gender-btn {
  background-color: black;
  color: white;
  width: 100px;
  height: 50px;
  border-radius: 2rem;
  margin: 5px;
}
.genre-btn:hover,
.gender-btn:hover {
  transition: background-color 0.3s;
  background-color: #424242;
  opacity: 85%;
}
.genre-btn.selected,
.gender-btn.selected {
  background-color: #424242;
  opacity: 85%;
}
</style>
