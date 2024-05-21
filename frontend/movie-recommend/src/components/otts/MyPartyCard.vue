<template>
  <div class="content-container">
    <img class="left-arrow" src="@/assets/arrow-left-circle.svg"/>
    <div class="contents">
      <p class="title">내가 만든 파티</p>
      <div class="content">
        <div class="join-btn">
          <img src="@/assets/person-add.svg" alt="">
          <p class="description">파티 생성하기!</p>
        </div>
        <p>내가 만든 파티가 아직 없어요!</p>
      </div>
      <MyPartyCreated />
      <hr>
      <p class="title">내가 참여중인 파티</p>
      <div class="content"> 
      <div class="join-btn">
        <img src="@/assets/box-arrow-in-right.svg" alt="">
        <p class="description">파티 참여하기!</p>
      </div>
      <p>내가 참여중인 파티가 아직 없어요!</p>
    </div>
      <MyPartyJoined />
    </div>
  </div>
</template>

<script setup>
import MyPartyCreated from '@/components/otts/MyPartyCreated.vue';
import MyPartyJoined from '@/components/otts/MyPartyJoined.vue';
</script>

<style scoped>
.content-container {
  border: 1px solid #595959;
  border-radius: 2rem;

  width: min(75%, 1000px);
  height: 80%;
}

.left-arrow {
  width: 45px;
  height: 45px;

  margin-top: 5%;
  margin-left: 5%;
}

.contents {;
  width: 80%;
  margin-left: 10%;
}

.title {
  font-size: 24px;
  font-weight: bold;

  margin-top: min(5%, 30px);
  margin-bottom: min(5%, 30px);
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.join-btn {
  border: 1px solid #595959;
  border-radius: 1rem;

  display: flex;
  align-items: center;
  justify-content: center;

  width: 265px;
  height: 78px;

  padding-right: 55px;

  margin-bottom: 10px;

  padding-left: 40px;
  padding-right: 55px;
}

.description {
  margin-bottom: 0px;
  font-size: 18px;

  margin-left: auto;
}
</style>