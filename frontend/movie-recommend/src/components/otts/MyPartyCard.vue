<template>
  <div class="content-container">
    <img class="left-arrow" src="@/assets/arrow-left-circle.svg"/>
    <div class="contents">
      <MyPartyCreated />
      <hr>
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
</style>