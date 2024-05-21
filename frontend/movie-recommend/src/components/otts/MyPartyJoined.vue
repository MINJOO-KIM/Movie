<template>
  <div>
    <p class="title">내가 참여중인 파티</p>
    <!-- 참여 중인 파티 없을 때 -->
    <div class="content"> 
      <div class="join-btn">
        <img src="@/assets/box-arrow-in-right.svg" alt="">
        <p class="description">파티 참여하기!</p>
      </div>
      <p>내가 참여중인 파티가 아직 없어요!</p>
    </div>

    <!-- 참여 중인 파티 있을 때 -->
  </div>
</template>

<script setup>
</script>

<style scoped>
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