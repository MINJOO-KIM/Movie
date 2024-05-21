<template>
  <div>
    <div class="title">플랫폼 정보를 입력해주세요</div>
    <div class="recommend-input">
      <form @submit.prevent="submitForm">
        <div class="platforms">
          <div>플랫폼</div>
          <div v-for="platform in platforms" :key="platform.id">
            <button
              type="button"
              :class="[
                'platform-btn',
                { selected: selectedPlatform === platform.id },
              ]"
              @click="selectPlatform(platform.id)"
            >
              <img
                :src="getPlatformImage(platform.name)"
                :alt="platform.name"
                class="platform-image"
              />
            </button>
          </div>
        </div>
        <!-- 인원 입력 -->
        <div class="people">
          <label for="people">인원</label>
          <input type="number" id="people" v-model="people" min="1" />
        </div>
        <!-- 가격 입력 -->
        <div class="price">
          <label for="price">가격</label>
          <input type="number" id="price" v-model="price" min="0" />
        </div>
        <!-- 계정 아이디 입력 -->
        <div class="account-id">
          <label for="account-id">계정 아이디</label>
          <input type="text" id="account-id" v-model="accountId" />
        </div>
        <!-- 계정 비밀번호 입력 -->
        <div class="account-pw">
          <label for="account-pw">계정 비밀번호</label>
          <input type="password" id="account-pw" v-model="accountPw" />
        </div>
        <!-- 계좌번호 입력 -->
        <div class="account-number">
          <label for="account-number">계좌번호</label>
          <input type="text" id="account-number" v-model="bankAccount" />
        </div>
        <!-- 제출 버튼 -->
        <br /><br />
        <input type="submit" value="생성하기" />
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";
import { useMovieStore } from "@/stores/movie";
import { onMounted } from "vue";

import netflixImage from "@/assets/netflix.svg";
import watchaImage from "@/assets/watcha.svg";
import disneyplusImage from "@/assets/disneyplus.svg";

const API_URL = "http://127.0.0.1:8000";
const token = "";

const store = useMovieStore();
const { platforms, getPlatforms } = store;

onMounted(() => {
  getPlatforms();
});

const selectedPlatform = ref("");
const people = ref(1);
const price = ref(0);
const accountId = ref("");
const accountPw = ref("");
const bankAccount = ref("");

// 플랫폼 선택 함수
const selectPlatform = (platformId) => {
  selectedPlatform.value = platformId;
};

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

// 폼 제출 핸들러 함수
const submitForm = () => {
  const formData = {
    platform: selectedPlatform.value,
    id: accountId.value,
    password: accountPw.value,
    price: price.value,
    capacity: people.value,
    bankAccount: bankAccount.value,
  };

  axios({
    method: "POST",
    url: `${API_URL}/otts/parties/`,
    headers: {
      Authorization: `Token ${token}`,
    },
    data: formData,
  })
    .then((res) => {
      console.log(res.data);
    })
    .catch((err) => {
      console.error(err);
    });
};
</script>

<style scoped>
input {
  color: black;
}
.platform-btn {
  background-color: black;
  color: white;
  width: 50px;
  height: 50px;
  border-radius: 1rem;
  margin: 10px;
  transition: background-color 0.3s;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.platform-btn.selected {
  border: 1px solid white;
}
.platform-image {
  width: 50px;
  height: 50px;
  object-fit: fit;
}
</style>
