<template>
  <div class="card-content">
    <img :src="getPlatformImage(props.party.platformId)" :alt="props.party.partyId" />
    <div>{{props.party.price}}원</div>
    <div>{{props.party.participants}}명 / {{ props.party.capacity }}명</div>
    <button @click="joinParty(props.party.partyId)">참여하기</button>
  </div>
</template>

<script setup>
import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";
import axios from "axios";

const props = defineProps({
  party: {
    type: Object,
    required: true,
  },
});
const getPlatformImage=(platformId)=>{
  switch(platformId){
    case 1:
      return disneyplusImage;
    case 2:
      return watchaImage;
    case 3:
      return netflixImage;
  }
}

const API_URL = "http://127.0.0.1:8000";
const token = "af22974742877689b5f7a5523f8780396c2dfb9f";

const joinParty = (partyId) => {
  axios({
    method: "POST",
    url: `${API_URL}/otts/parties/${partyId}/join/`,
    headers: {
      Authorization: `Token ${token}`,
    },
    data: partyId,
  })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.error(err);
    });
}

console.log(props.party);
</script>

<style scoped>

</style>
