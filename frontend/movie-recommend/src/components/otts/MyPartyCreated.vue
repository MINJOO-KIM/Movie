<template>
  <div class="party-container">
    <!-- 만든 파티 있을 때 -->
    <div class="party-info">
      <img class="icon" src="@/assets/netflix.svg" alt="">
      <span>월 3,000원으로 4명이 참여하고 있어요!</span>
    </div>
    <div class="account-id">
      <label for="account-id">계정 ID</label>
      <input id="account-id" type="text" placeholder="ssafy1111@gmail.com">
    </div>
    <div class="account-pw">
      <label for="account-pw">계정 PW</label>
      <input id="account-pw" type="password" placeholder="**************">
    </div>
    <div class="last-info">
      <div class="bank-account">
        <label for="bank-account">계좌번호</label>
        <input id="bank-account" type="text" placeholder="신한 111-111-111111">
      </div>
      <button class="modify-btn">계정에 변화가 있나요?</button>
    </div>
    <hr>
  </div>             
</template>

<script setup>
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
}

input {
  margin-left: auto;
  background-color: transparent;

  border: 0;
  border-bottom: 1px solid #595959;
}

.modify-btn {
  background-color: #000000; 
  
  padding: 3px 10px;

  border: 1px solid #FFFFFF;
  border-radius: 10px;
}

.modify-btn:hover {
  background-color: #191919;
}



</style>