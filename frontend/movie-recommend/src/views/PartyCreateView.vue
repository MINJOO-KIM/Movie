<template>
  <div class="create-container">
    <div class="create-form">
      <div class="header">
        <img
          class="back"
          src="@/assets/arrow-left-circle.svg"
          alt=""
          @click="goback()"
        />
        <div class="title">새로운 파티를 생성해주세요!</div>
      </div>
      <div class="recommend-input">
        <form @submit.prevent="submitForm">
          <div class="platforms">
            <label>플랫폼</label>
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
            <div v-if="!selectedPlatform && showErrors" class="error">
              플랫폼은 필수 입력값입니다.
            </div>
          </div>
          <!-- 인원 입력 -->
          <div class="people">
            <label for="people">인원</label>
            <input type="text" id="people" v-model="people" min="1" />
            <svg
              width="15"
              height="27"
              viewBox="0 0 15 27"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <path
                @click="increasePeople"
                d="M7.5 0L13.9952 11.25H1.00481L7.5 0Z"
                fill="white"
              />
              <path
                @click="decreasePeople"
                d="M7.67135 26.25L1.17616 15L14.1665 15L7.67135 26.25Z"
                fill="white"
              />
            </svg>
            <div v-if="!people && showErrors" class="error">
              인원은 필수 입력값입니다.
            </div>
          </div>
          <!-- 가격 입력 -->
          <div class="price">
            <label for="price">가격</label>
            <input type="text" id="price" v-model="price" min="0" />원
            <div v-if="!price && showErrors" class="error">
              가격은 필수 입력값입니다.
            </div>
          </div>
          <!-- 계정 아이디 입력 -->
          <div class="account-id">
            <label for="account-id">계정 ID</label>
            <input type="text" id="account-id" v-model="accountId" />
            <div v-if="!accountId && showErrors" class="error">
              계정 ID는 필수 입력값입니다.
            </div>
          </div>
          <!-- 계정 비밀번호 입력 -->
          <div class="account-pw">
            <label for="account-pw">계정 PW</label>
            <input type="password" id="account-pw" v-model="accountPw" />
            <div v-if="!accountPw && showErrors" class="error">
              계정 PW는 필수 입력값입니다.
            </div>
          </div>
          <!-- 계좌번호 입력 -->
          <div class="account-number">
            <label for="account-number">계좌번호</label>
            <input type="text" id="account-number" v-model="bankAccount" />
            <div v-if="!bankAccount && showErrors" class="error">
              계좌번호는 필수 입력값입니다.
            </div>
          </div>
          <!-- 제출 버튼 -->
          <br /><br />
          <input class="create-btn" type="submit" value="생성하기" />
        </form>
      </div>
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
import { useRouter } from "vue-router";

const API_URL = "http://127.0.0.1:8000";

const store = useMovieStore();
const { platforms, getPlatforms } = store;
const router = useRouter();
const goback = function () {
  router.go(-1);
};

onMounted(() => {
  getPlatforms();
});

const selectedPlatform = ref("");
const people = ref(1);
const price = ref(0);
const accountId = ref("");
const accountPw = ref("");
const bankAccount = ref("");
const showErrors = ref(false);

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

// 인원 증감 함수
const increasePeople = function () {
  people.value++;
};

const decreasePeople = function () {
  if (people.value > 0) people.value--;
};

// 폼 제출 핸들러 함수
const submitForm = () => {
  showErrors.value = true;

  if (
    !selectedPlatform.value ||
    !accountId.value ||
    !accountPw.value ||
    !price.value ||
    !people.value ||
    !bankAccount.value
  ) {
    return;
  }

  const formData = {
    platform: selectedPlatform.value,
    account_id: accountId.value,
    account_password: accountPw.value,
    price: price.value,
    capacity: people.value,
    bank_account: bankAccount.value,
  };

  axios({
    method: "POST",
    url: `${API_URL}/otts/parties/`,
    headers: {
      Authorization: `Token ${localStorage.getItem("token")}`,
    },
    data: formData,
  })
    .then((res) => {
      router.push("/mypage");
      console.log(res.data);
    })
    .catch((err) => {
      console.error(err);
      if (err.response.status === 401) {
            store.solveUnAuthorized(err);
          }
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
  width: 47px;
  height: 50px;
  object-fit: fit;
}

.create-container {
  display: flex;
  align-items: center;
  justify-content: center;

  height: 90vh;
}

.create-form {
  border: 1px solid #595959;
  border-radius: 2rem;

  width: min(70%, 1000px);
  height: 660px;

  display: flex;
  flex-direction: column;

  padding: 40px;
  overflow: auto;
}

.header {
  display: flex;
  align-items: center;

  justify-content: center;

  position: relative;

  margin-top: 10px;
}

.back {
  width: 45px;
  height: 45px;

  position: absolute;
  left: 0px;
}

.title {
  font-size: 32px;
  font-weight: bold;
}

.recommend-input {
  margin-left: 15%;
  margin-right: 15%;
}

.platforms,
.people,
.price,
.account-id,
.account-pw,
.account-number {
  display: flex;
  align-items: center;
}

.platforms {
  margin-top: 60px;
}

.price,
.account-id,
.account-pw,
.account-number {
  margin-top: 30px;
}

label {
  font-size: 20px;
  font-weight: bold;
}

.platforms > label {
  margin-right: 55px;
}

.people {
  margin-top: 20px;
}

.people > label {
  margin-right: 85px;
}

.people > input {
  width: 65px;
  height: 30px;

  background-color: black;
  color: white;

  border: 1px solid #ffffff;
  border-radius: 1rem;

  text-align: center;

  margin-right: 6px;
}

path {
  cursor: pointer;
}

.price > label {
  margin-right: 85px;
}

.price > input {
  width: 100px;
  margin-right: 3px;
}

.account-id > label {
  margin-right: 60px;
}

.account-pw > label {
  margin-right: 50px;
}

.account-number > label {
  margin-right: 50px;
}

.price > input,
.account-id > input,
.account-pw > input,
.account-number > input {
  background-color: transparent;
  color: white;

  border-width: 0px;
  border-bottom: 1px solid #595959;

  outline: none;
}

.account-id > input,
.account-pw > input,
.account-number > input {
  width: 300px;
}

.create-btn {
  width: 100%;
  background-color: black;
  color: white;

  border: 1px solid #ffffff;
  border-radius: 1rem;

  height: 50px;

  font-size: 18px;
  font-weight: bold;
}

.create-btn:hover {
  background-color: #171717;
}

.error {
  color: red;
  font-size: 14px;
  margin-left: 10px;
}
</style>
