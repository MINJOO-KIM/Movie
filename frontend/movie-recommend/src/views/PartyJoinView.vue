<template>
  <div class="outer">
  <div class="party-join-container">
    <div class="party-join-card">
      <div class="header">
        <img class="back" src="@/assets/arrow-left-circle.svg" alt="" @click="goback()">
        <h2>파티에 자유롭게 참여하세요!</h2>
      </div>
      <div class="search-bar">
        <div class="platform-choice">
          <div v-for="platform in platforms" :key="platform.id" class="platform-checkbox">
            <input 
              type="checkbox" 
              :id="'platform-' + platform.id" 
              :value="platform.id" 
              v-model="selectedPlatforms"
            />
            <label :for="'platform-' + platform.id">
              <img :src="getPlatformImage(platform.name)" :alt="platform.name" />
            </label>
          </div>
        </div>
        <button class="search-btn" @click="fetchParties(selectedPlatforms.join(','))">조회</button>
      </div>
      <div class="party-container">
        <div v-for="party in parties" :key="party.id" class="col">
          <PartyCard :party="party" />
        </div>
      </div>
      
    </div>
  </div>
</div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
import axios from 'axios';
import { onMounted } from 'vue';
import PartyCard from '@/components/otts/PartyCard.vue'
import { useRouter } from 'vue-router';

import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";

const store = useMovieStore();
const { platforms, getPlatforms } = store;
const router = useRouter()
const goback = function() {
  router.go(-1);
}

function getPlatformImage(platformName) {
  switch (platformName.toLowerCase()) {
    case "disneyplus":
      return disneyplusImage;
    case "netflix":
      return netflixImage;
    case "watcha":
      return watchaImage;
  }
}

onMounted(() => {
  getPlatforms();
});

const parties = ref({});
const selectedPlatforms = ref([]);
const API_URL = "http://127.0.0.1:8000";
const fetchParties = (platformsId) => {
  axios({
    method: "GET",
    url: `${API_URL}/otts/parties/`,
    params: {
      platforms: platformsId,
    },
    headers: {
      Authorization: `Token ${localStorage.getItem('token')}`
    }
  })
    .then((res) => {
      console.log(res);
      parties.value = res.data;
      // console.log(parties)
    })
    .catch((err) => console.log(err));
};
console.log(parties)
</script>

<style scoped>
.outer {
  display: flex;
  justify-content: center;
}

.party-join-container {
  display: flex;
  flex-direction: column;
  justify-content: center;

  align-items: center;
  border: 1px solid #595959;
  border-radius: 2rem;

  width: min(80vw, 1010px);
  min-width: 600px;
  height: 700px;

  margin-top: 15vh;
}

.party-join-card {
  width: 80%;
  height: 80%;
}

.header {
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;

  position: relative;
}

.back {
  width: 45px;
  height: 45px;

  position: absolute;
  left: 0;
}

.search-bar,
.platform-choice {
  display: flex;
}

.search-bar {
  margin-top: 60px;
  margin-bottom: 50px;
}

.platform-choice {
  margin-right: auto;
}

.search-bar label {
  margin-left: 15px;
  margin-right: 20px;
}

.platform-checkbox {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.platform-checkbox img {
  width: 30px;
  height: 30px;
  margin-right: 10px;
}

.search-btn {
  width: 50px;
  height: 30px;

  background-color: black;
  border: 1px solid #595959;
  border-radius: 10px;
}

.search-btn:hover {
  background-color: rgba(74, 74, 74, 0.35);
}

.party-container {
  height: 65%;
  overflow: auto;
}

.party-container::-webkit-scrollbar {
    width: 40px; /* 스크롤바의 너비 */
}

.party-container::-webkit-scrollbar-thumb {
    height: 75%; /* 스크롤바의 길이 */
    background: #595959; /* 스크롤바의 색상 */
    background-clip: padding-box;
    border: 17px solid #000000;
    border-radius: 50px;
}

.party-container::-webkit-scrollbar-track {
    background: #000000; /*스크롤바 뒷 배경 색상*/
}


.col {
  margin-bottom: 20px;
}
</style>
