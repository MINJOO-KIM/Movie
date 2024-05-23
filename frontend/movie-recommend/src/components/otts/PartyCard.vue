<template>
  <div class="card-content">
    <div class="left-info">
      <img class="icon" :src="getPlatformImage(props.party.platformId)" :alt="props.party.partyId" />
      <div class="name-price">
        <span class="platform-name">{{getPlatformName(props.party.platformId)}}</span>
        <img class="coin" src="@/assets/coin.svg" alt="">
        <div>{{props.party.price}}원</div>
      </div>
    </div>
    <div class="right-info">
      <div>{{props.party.participants}}명 / {{ props.party.capacity }}명</div>
      <button @click="joinParty(props.party.partyId)">참여하기</button>
    </div>
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

const getPlatformName = (platformId) => {
  switch(platformId) {
    case 1:
      return '디즈니+';
    case 2:
      return '왓챠';
    case 3:
      return '넷플릭스';
  }
}

const API_URL = "http://127.0.0.1:8000";

const joinParty = (partyId) => {
  axios({
    method: "POST",
    url: `${API_URL}/otts/parties/${partyId}/join/`,
    headers: {
      Authorization: `Token ${store.token}`,
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
.card-content {
  border: 1px solid #FFFFFF;
  border-radius: 1rem;

  width: 100%;
  height: 75px;
  min-width: 500px;

  display: flex;
  justify-content: space-between;
  align-items: center;

  padding-left: 22px;
  padding-right: 30px;
}

.card-content > div {
  display: flex;
  align-items: center;
}

.left-info {
  margin-right: auto;
}

.icon {
  margin-right: 12px;
}

.name-price {
  width: 150px;
  
  display: flex;
}

.platform-name {
  margin-right: auto;
}

.coin {
  margin-right: 3px;
}

.right-info > button {
  margin-left: 24px;

  background-color: black;

  width: 77px;
  height: 31px;

  border: 1px solid #FFFFFF;
  border-radius: 10px;
}

.right-info > button:hover {
  background-color: #191919;
}
</style>
