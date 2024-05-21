<template>
  <div class="party-container">
    <!-- 만든 파티 있을 때 -->
    <div class="party-info">
      <img src="@/assets/netflix.svg" alt="">
      <span>월 Price원으로 N명이 참여하고 있어요!</span>
    </div>
    <div>
      <label for="account-id">계정 ID</label>
      <input id="account-id" type="text" placeholder="ssafy1111@gmail.com">
    </div>
    <div>
      <label for="account-pw">계정 PW</label>
      <input id="account-pw" type="password" placeholder="**************">
    </div>
    <div>
      <div>
        <label for="bank-account">계좌번호</label>
        <input id="bank-account" type="text" placeholder="신한 111-111-111111">
      </div>
      <button>계정에 변화가 있나요?</button>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped> 
</style>