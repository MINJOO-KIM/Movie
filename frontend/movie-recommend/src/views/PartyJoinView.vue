<template>
  <div>
    PartyJoinView
    <div class="party-join-card">
      <h2>파티에 자유롭게 참여하세요!</h2>
      <div>
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

      <button @click="fetchParties(selectedPlatforms.join(','))">조회</button>
      <div v-for="party in parties" :key="party.id" class="col">
        <PartyCard :party="party" />
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

import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";

const store = useMovieStore();
const { platforms, getPlatforms } = store;

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
.party-join-card {
  margin: 20px;
}

.platform-checkbox {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
}

.platform-checkbox img {
  width: 50px;
  height: 50px;
  margin-right: 10px;
}
</style>
