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
    const storeBestMovie = ref("");

    const API_URL = "http://127.0.0.1:8000";
    const token = "af22974742877689b5f7a5523f8780396c2dfb9f"

    const getRecommendMovies = function (params) {
      axios({
        method: "GET",
        url: `${API_URL}/movies/recommend`,
        params: params,
      })
        .then((res) => {
          console.log(res);
          movies.value = res.data;
        })
        .catch((err) => console.log(err));
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

    const getParties = function() {
      axios({
        method:"GET",
        url: `${API_URL}/accounts/`,
        headers: {
          Authorization: `Token ${token}`,
        },
      })
        .then((res)=>{
          console.log(res);
          parties.value = res.data;
        })
        .catch((err)=>{
          console.log(err);
        })
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
      storeBestMovie,
    };
  },
  { persist: true }
);
