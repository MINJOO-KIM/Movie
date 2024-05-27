<template>
  <div class="party-container">
    <div v-for="(party, index) in ownParties" :key="party.id">
      <div class="party-info">
        <img class="icon" :src="getPlatformImage(party.platform)" alt="">
        <span>월 {{ party.price }}원으로 {{party.capacity}}명이 참여하고 있어요!</span>
      </div>
      <div class="account-id">
        <label :for="'account-id-' + index">계정 ID</label>
        <input :disabled="!isModyfing[index]" :id="'account-id-' + index" type="text" v-model="party.account_id">
      </div>
      <div class="account-pw">
        <label :for="'account-pw-' + index">계정 PW</label>
        <input :disabled="!isModyfing[index]" :id="'account-pw-' + index" type="password" v-model="party.account_password">
      </div>
      <div class="last-info">
        <div class="bank-account">
          <label :for="'bank-account-' + index">계좌번호</label>
          <input :disabled="!isModyfing[index]" :id="'bank-account-' + index" type="text" v-model="party.bank_account">
        </div>
        <button v-if="!isModyfing[index]" class="modify-btn" @click="startModifying(index)">계정에 변화가 있나요?</button>
        <button v-else class="modifying-btn" @click="updateAccount(party, index)">수정하기</button>
      </div>
      <hr>
    </div>
  </div>             
</template>

<script setup>
import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import axios from "axios";
import { useMovieStore } from "@/stores/movie";

const router = useRouter();
const isModyfing = ref([]);
const store = useMovieStore();

const props = defineProps({
  ownParties: {
    type: Array,
    required: true
  }
});

onMounted(() => {
  isModyfing.value = props.ownParties.map(() => false);
});

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

const API_URL = "http://127.0.0.1:8000";
const startModifying = (index) => {
  isModyfing.value[index] = true;
};

const updateAccount = (party, index) => {
  const updatedAccount = {
    id: party.account_id,
    password: party.account_password,
    bankAccount: party.bank_account,
  };

  axios({
    method: "PUT",
    url: `${API_URL}/otts/parties/${party.id}/`,
    headers: {
      Authorization: `Token ${localStorage.getItem('token')}`,
    },
    data: updatedAccount,
  })
    .then((res) => {
      console.log(res.data);
      isModyfing.value[index] = false; 
    })
    .catch((err) => {
      console.error(err);
      if (err.response.status === 401) {
        store.solveUnAuthorized(err);
      } else if (err.response.status === 404) {
        window.alert(err.response.data.message);
        router.go(0);
      } else {
        window.alert(err.response.data.message);
        router.push({name: 'OTTHomeView'});
      }
    });
};
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