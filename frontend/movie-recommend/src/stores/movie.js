import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useMovieStore = defineStore(
  "movie",
  () => {
    const movies = ref([]);
    const genres = ref([]);
    const platforms = ref([]);
    const parties = ref([]);
    const storedParams = ref({
      bestMovie: "",
      genres: "",
      directors: "",
      actors: "",
      recommended: "",
      submitted: false,
    });

    const API_URL = "http://127.0.0.1:8000";
    const token = ref(null)

    const getRecommendMovies = function (params) {
      return axios({
        method: "GET",
        url: `${API_URL}/movies/recommend`,
        params: params,
      })
        .then((res) => {
          console.log(res);
          movies.value = res.data;
          return res.data.map((movie) => movie.movieId.toString()); // 추천된 영화의 ID 목록을 문자열로 반환
        })
        .then((recommendedIds) => {
          const recommended = recommendedIds.join(","); // 문자열로 변환
          const updatedRecommended = storedParams.value.recommended
            ? `${storedParams.value.recommended},${recommended}` // 기존 추천영화ID, 새로운 추천영화ID
            : recommended;
          updateStoredParams({
            ...params,
            recommended: updatedRecommended,
            submitted: true,
          });
        })
        .catch((err) => {
          console.log(err);
          return [];
        });
    };

    const getGenres = function () {
      axios({
        method: "GET",
        url: `${API_URL}/movies/genres`,
      })
        .then((res) => {
          console.log(res);
          genres.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getPlatforms = function () {
      axios({
        method: "GET",
        url: `${API_URL}/otts/platforms`,
      })
        .then((res) => {
          console.log(res);
          platforms.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const getParties = function () {
      axios({
        method: "GET",
        url: `${API_URL}/accounts/`,
        headers: {
          Authorization: `Token ${token.value}`,
        },
      })
        .then((res) => {
          console.log(res);
          parties.value = res.data;
        })
        .catch((err) => {
          console.log(err);
        });
    };

    const updateStoredParams = (params) => {
      storedParams.value = { ...storedParams.value, ...params };
    };

    const resetParams = () => {
      storedParams.value = {
        bestMovie: "",
        genres: "",
        directors: "",
        actors: "",
        recommended: "",
        submitted: false, // Keep submitted as false
      };
    };

    const signUp = function (payload) {
      // 1. 사용자 입력 데이터를 받아
      const username = payload.username
      const password1 = payload.password1
      // const { username, password1} = payload
  
      // 2. axios로 django에 요청을 보냄
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1,
        }
      })
       .then((response) => {
         console.log('회원가입 성공!')
         const password = password1
         logIn({ username, password })
       })
       .catch((error) => {
         console.log(error)
       })
    }

    return {
      movies,
      getRecommendMovies,
      genres,
      getGenres,
      platforms,
      getPlatforms,
      parties,
      getParties,
      storedParams,
      updateStoredParams,
      resetParams,
      signUp,
      token,
    };
  },
  { persist: true }
);
