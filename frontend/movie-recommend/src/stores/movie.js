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
    const token = "af22974742877689b5f7a5523f8780396c2dfb9f";

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
          Authorization: `Token ${token}`,
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
    };
  },
  { persist: true }
);
