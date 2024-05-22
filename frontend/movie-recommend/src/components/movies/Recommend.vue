<template>
  <div class="research-box">
    <div class="background">
    </div>
    <p class="title">당신의 취향을 알려주세요</p>
    <div class="recommend-input">
      <form @submit.prevent="submitForm">
        <div class="gender">
          <label>성별:</label>
          <button
            type="button"
            :class="['gender-btn', { selected: gender === 'male' }]"
            @click="selectGender('male')"
          >
            남
          </button>
          <button
            type="button"
            :class="['gender-btn', 'female-btn',{ selected: gender === 'female' }]"
            @click="selectGender('female')"
          >
            여
          </button>
          <li>필수 입력값입니다</li>
        </div>
        <div class="age">
          <label for="age">나이:</label>
          <input class="age-input-box" type="text" id="age" name="age" v-model="age" min="0" />
          <svg width="15" height="27" viewBox="0 0 15 27" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path @click="increaseAge" d="M7.5 0L13.9952 11.25H1.00481L7.5 0Z" fill="white"/>
            <path @click="decreaseAge" d="M7.67135 26.25L1.17616 15L14.1665 15L7.67135 26.25Z" fill="white"/>
          </svg>
          <li>필수 입력값입니다</li>
        </div>
        <div class="best-movie">
          <label for="best-movie">최근에 재미있게 본 영화</label>
          <input type="text" id="best-movie" v-model="bestMovie" />
          <li>필수 입력값입니다</li>
        </div>
        <div class="genres">
          <label>선호하는 장르</label>
          <div class="genre-container">
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
        <input class="submit-btn" type="submit" value="제출하기!" />
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

// 나이 up-down
const increaseAge = function() {
  age.value++;
}

const decreaseAge = function() {
  if (age.value > 0) {
    age.value--;
  }
}

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
.research-box {
  border: 1px solid #FFFFFF;
  border-radius: 2rem;

  width: 60vw;
  margin-left: 20vw;
  padding: 5%;
  padding-top: 55px;
  padding-bottom: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;

  background-color: rgba(0, 0, 0, 0.5);
}


.recommend-input {
  width: 80%; 
}

.title {
  font-size: 27px;
  font-weight: bold;
  margin-bottom: 55px;
}

label {
  font-size: 18px;
  font-weight: bold;
}

input { 
  color: black;
}

li {
  margin-left: auto;
}

.gender,
.age,
.best-movie {
  display: flex;
  align-items: center;
}

.genre-btn,
.gender-btn {
  background-color: black;
  color: white;
  width: 65px;
  height: 30px;
  border-radius: 2rem;
  border: 1px solid #FFFFFF;
  margin-left: 40px;
}

.genre-btn {
  width: 100px;
  margin-left: 25px;
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

.female-btn {
  margin-left: 10px;
}

.age {
  margin-top: 30px;
  margin-bottom: 0px;
}

.age-input-box {
  width: 65px;
  height: 30px;
  
  margin-left: 40px;
  margin-right: 6px;

  background-color: black;
  color: white;

  border: 1px solid #FFFFFF;
  border-radius: 2rem;

  text-align: center;
}

path {
  cursor: pointer;
}

.best-movie {
  margin-top: 40px;
}

.best-movie > input,
.directors > input,
.actors > input {
  margin-left: 27px;
  background-color: rgba(0, 0, 0, 0);
  border-width: 0px;
  border-bottom: 1px solid white;

  color: white;
  width: 70%;
  
  margin-right: 30px;
  outline: none;
}

.best-movie > input {
  width: 50%;
}

.genres {
  margin-top: 40px;
}

.genre-container {
  display: flex;
  justify-content: flex-start;

  flex-wrap: wrap;
  gap: 10px;

  margin-top: 20px;
}

.directors {
  margin-top: 40px;
}

.actors {
  margin-top: 40px;
}

.submit-btn {
  width: 100%;
  
  color: white;
  background-color: black;

  border: 1px solid #FFFFFF;
  border-radius: 1rem;

  height: 50px;

  font-size: 18px;
  font-weight: bold;
}

.submit-btn:hover {
  transition: background-color 0.3s;
  background-color: #424242;
  opacity: 85%;
}
</style>
