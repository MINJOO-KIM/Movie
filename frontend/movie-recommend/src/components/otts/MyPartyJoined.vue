<template>
  <div class="party-container">
    <div v-for="(party, index) in participateParties" :key="party.id" style="margin-bottom: 20px;">
      <div class="summary-infos">
        <div class="left-context">
          <img class="icon" :src="getPlatformImage(party.platform)" alt="">
          <span class="platform-name">{{ getPlatformName(party.platform) }}</span>
          <div class="price">
            <img src="@/assets/coin.svg" alt="">
            <span>{{ party.price }}원</span>
          </div>
        </div>
        <div class="right-context">
          <p>{{ party.participants }}명 / {{ party.capacity }}명</p>
          <img class="toggle-btn" src="@/assets/caret-down-square.svg" alt="" @click="toggleDetails(index)">
        </div>
      </div>

      <div class="account-infos" v-if="isShow[index]">
        <div class="account-id">
          <label :for="'account-id-' + index">계정 ID</label>
          <input disabled :id="'account-id-' + index" type="text" :placeholder="party.account_id">
        </div>
        <div class="account-pw">
          <label :for="'account-pw-' + index">계정 PW</label>
          <input disabled :id="'account-pw-' + index" type="password" :placeholder="party.account_password">
        </div>
        <div class="last-info">
          <div class="bank-account">
            <label :for="'bank-account-' + index">계좌번호</label>
            <input disabled :id="'bank-account-' + index" type="text" :placeholder="party.bank_account">
          </div>
          <button class="leave-btn" @click="withdrawParty(party)">파티탈퇴</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";
import axios from 'axios';
import router from '@/router';

const props = defineProps({
  participateParties: {
    type: Array,
    required: true
  }
});

const isShow = ref(props.participateParties.map(() => false));

const toggleDetails = (index) => {
  isShow.value[index] = !isShow.value[index];
};

const getPlatformImage = (platformId) => {
  switch(platformId) {
    case 1:
      return disneyplusImage;
    case 2:
      return watchaImage;
    case 3:
      return netflixImage;
  }
};

const getPlatformName = (platformId) => {
  switch(platformId) {
    case 1:
      return "디즈니+";
    case 2:
      return "왓챠";
    case 3:
      return "넷플릭스";
  }
};

const API_URL = "http://127.0.0.1:8000";
const withdrawParty = (party) => {
  axios({
    method:"DELETE",
    url:`${API_URL}/otts/parties/${party.id}/withdraw/`,
    headers:{
      Authorization: `Token ${localStorage.getItem('token')}`,
    },
  })
    .then((res)=>{
      console.log(res.data);
      router.go(0)
    })
    .catch((err)=>{
      console.error(err);
    })
};

</script>

<style scoped>
.summary-infos {
  display: flex;
  align-items: center;
  height: 75px;
  padding: 25px;
  border: 1px solid white;
  border-radius: 1rem;
}

.left-context {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-right: auto;
}

.platform-name {
  margin-left: 20px;
}

.price {
  margin-left: 20px;
}

.price > span {
  margin-left: 5px;
}

.right-context {
  display: flex;
  align-items: center;
}

.right-context > p {
  width: 90px;
  margin: 0;
}

.toggle-btn {
  cursor: pointer;
}

.account-infos {
  display: flex;
  flex-direction: column;
  gap: 15px;
  padding: 20px 50px;
  border: 1px solid #595959;
  border-radius: 1rem;
}

.account-id,
.account-pw,
.bank-account {
  display: flex;
  width: 300px;
}

.last-info {
  display: flex;
  justify-content: space-between;
}

label {
  font-size: 15px;
  font-weight: bold;
}

input {
  margin-left: auto;
  background-color: transparent;
  border: 0;
  border-bottom: 1px solid #595959;
}

.leave-btn {
  background-color: #000000;
  padding: 3px 10px;
  border: 1px solid #FFFFFF;
  border-radius: 10px;
}

.leave-btn:hover {
  background-color: #191919;
}
</style>