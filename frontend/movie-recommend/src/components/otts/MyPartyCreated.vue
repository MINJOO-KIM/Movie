<template>
  <div class="party-container">
    <!-- 만든 파티 있을 때 -->
    <div v-for="party in ownParties" :key="party.id">
      <div class="party-info">
        <img class="icon" :src="getPlatformImage(party.platform)" alt="">
        <span>월 {{ party.price }}원으로 {{party.capacity}}명이 참여하고 있어요!</span>
      </div>
      <div class="account-id">
        <label for="account-id">계정 ID</label>
        <input :disabled="!isModyfing" id="account-id" type="text" :placeholder="party.account_id">
      </div>
      <div class="account-pw">
        <label for="account-pw">계정 PW</label>
        <input :disabled="!isModyfing" id="account-pw" type="password" :placeholder="party.account_password">
      </div>
      <div class="last-info">
        <div class="bank-account">
          <label for="bank-account">계좌번호</label>
          <input :disabled="!isModyfing" id="bank-account" type="text" :placeholder="party.bank_account">
        </div>
        <button v-if="!isModyfing" class="modify-btn" @click="isModyfing=true">계정에 변화가 있나요?</button>
        <button v-else class="modifying-btn" @click="isModyfing=false">수정하기</button>
      </div>
      <hr>
    </div>
  </div>             
</template>

<script setup>
import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";
import { ref } from 'vue';

const isModyfing = ref(true);

const props = defineProps({
  ownParties: {
    type: Array,
    required: true
  }
})

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

// 수정하기 버튼 클릭 시에는 axios 요청도 보낼 수 있게 해주세요

</script>

<style scoped>
.party-container {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.icon {
  width: 35px;
  height: 35px;
  margin-bottom: 20px;
}

.party-info > span {
  margin-left: 20px;

  font-size: 20px;
  font-weight: bold;
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
  margin-top: 10px;
}

input {
  margin-left: auto;
  background-color: transparent;

  border: 0;
  border-bottom: 1px solid #595959;

  outline: none;
}

.modify-btn,
.modifying-btn {
  background-color: #000000; 
  
  padding: 3px 10px;

  border: 1px solid #FFFFFF;
  border-radius: 10px;
}

.modifying-btn {
  color: #FF0000;
  font-weight: bold;

  width: 150px;
}

.modify-btn:hover,
.modifying-btn:hover {
  background-color: #191919;
}



</style>