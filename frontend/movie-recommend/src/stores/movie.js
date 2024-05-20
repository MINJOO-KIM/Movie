import { ref, computed } from "vue";
import { defineStore } from "pinia";
import axios from "axios";

export const useMovieStore = defineStore(
  "movie",
  () => {
    const movies = ref([]);
    const API_URL = "http://127.0.0.1:8000";

    const getRecommendMovies = function () {
      axios({
        method: "get",
        url: `${API_URL}/movies/recommend`,
      })
        .then((res) => {
          console.log(res);
          movies.value = res.data;
        })
        .catch((err) => console.log(err));
    };

    
    return { movies, getRecommendMovies };
  },
  { persist: true }
);
