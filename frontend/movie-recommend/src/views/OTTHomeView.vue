<template>
  <div class="content-container">
    <h1>OTT 공유 서비스</h1>
    <div class="platform-icon-container">
      <img src="@/assets/netflix.svg" alt="" class="platform-icon">
      <img src="@/assets/watcha.svg" alt="" class="platform-icon">
      <img src="@/assets/disneyplus.svg" alt="" class="platform-icon">
    </div>

    <div class="description">
        넷플릭스, 왓챠, 디즈니플러스까지!<br>
        매달 나가는 구독료 부담스럽지 않게! 내가 보고싶은 영화는 마음대로!<br>
        안전하게 계정을 공유하는 OTT 공유 서비스를 이용해보세요!
    </div>

    <div class="party-btn-container">
      <RouterLink :to="{name: 'PartyCreateView'}">
        <div class="party-btn">
          <img src="@/assets/person-add.svg" alt="" class="btn-icon">
          <span>파티 생성하기!</span>
        </div>
      </RouterLink>
      <RouterLink :to="{name: 'PartyJoinView'}">
        <div class="party-btn">
          <img src="@/assets/box-arrow-in-right.svg" alt="" class="btn-icon">
          <span>파티 참여하기!</span>
        </div>
      </RouterLink>
    </div>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
.content-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  
  padding-top: 220px;
  
  background-color: black;
  height: 90vh;
}

.platform-icon-container {
  margin-top: 22px;
  margin-bottom: 22px;
}

.platform-icon {
  margin-right: 12px;
}

.description {
  text-align: center;
  margin-bottom: 75px;
  font-size: 20px;
}

.party-btn-container {
  display: flex;
  gap: 50px;
  flex-wrap: wrap;
  justify-content: center;
}

.party-btn {
  background-color: #000000;
  width: 265px;
  height: 70px;
  
  border: 1px solid #AAAAAA;
  border-radius: 15px;

  padding-left: 38px;

  display: flex;
  align-items: center;

  cursor:pointer;
}

.party-btn:hover {
  background-color: #191919;
}

.btn-icon {
  width: 40px;
  height: 40px;

  margin-right: 20px;
}

a {
  text-decoration: none;
}
</style>