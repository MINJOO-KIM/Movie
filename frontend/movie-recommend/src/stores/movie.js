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
        submitted: false, 
      };
    };

    const signUp = function (payload) {
      const username = payload.username
      const password = payload.password
  
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password,
        }
      })
       .then((response) => {
         console.log('회원가입 성공!')
       })
       .catch((error) => {
         console.log(error)
       })
    }

    const logIn = function (payload) {
      const { username, password } = payload
      console.log(username)
      console.log(password)
      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
        .then((res) => {
          token.value = res.data.key
          router.push({ name : 'OTTHomeView' })
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
      logIn,
      token,
    };
  },
  { persist: true }
);
