<template>
  <div class="party-container">
    <!-- 참여 중인 파티 있을 때 -->
    <div class="summary-infos">
      <div class="left-context">
        <img class="icon"  src="@/assets/watcha.svg" alt="">
        <span class="platform-name">왓챠</span>
        <div class="price">
          <img src="@/assets/coin.svg" alt="">
          <span>3000원</span>
        </div>
      </div>
      <div class="right-context">
        <p>2명 / 4명</p>
        <img class="toggle-btn" src="@/assets/caret-down-square.svg" alt="" @click="isShow = !isShow">
      </div>
    </div>

    <div class="account-infos" v-if="isShow">
      <div class="account-id">
        <label for="account-id">계정 ID</label>
        <input id="account-id" type="text" placeholder="ssafy1111@gmail.com">
      </div>
      <div class="account-pw">
        <label for="account-pw">계정 PW</label>
        <input id="account-pw" type="password" placeholder="***************">
      </div>
      <div class="last-info">
        <div class="bank-account">
          <label for="bank-account">계좌번호</label>
          <input id="back-account" type="text" placeholder="신한 111-111-111111">
        </div>
        <button class="leave-btn">파티탈퇴</button>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const isShow = ref(false);
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

.right-context > p{
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