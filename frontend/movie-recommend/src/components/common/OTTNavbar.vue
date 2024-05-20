<template>
  <header>
    <nav class="navbar navbar-expand-lg custom-navbar-bg fixed-top" data-bs-theme="dark">
      <div class="container-fluid">
        <!-- <RouterLink to="/" class="navbar-brand">
          <img :src="logo" alt="Logo" height="30" />
        </RouterLink> -->
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNavAltMarkup"
          aria-controls="navbarNavAltMarkup"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
          <div class="navbar-nav ms-auto d-flex" style="color: white">
            <RouterLink to="/otts" class="nav-link" active-class="active-tab"
              >OTT 공유
            </RouterLink>
            <RouterLink to="/" class="nav-link" active-class="active-tab"
              >영화추천
            </RouterLink>
            <!-- 로그인하지 않은 상태일 때 -->
            <RouterLink v-if="!isAuthenticated" to="/login" class="nav-link" active-class="active-tab"
              >로그인
            </RouterLink>
            <RouterLink v-if="!isAuthenticated" to="/signup" class="nav-link" active-class="active-tab"
              >회원가입
            </RouterLink>

            <!-- 로그인 한 상태일 때 -->
            <form v-if="isAuthenticated" class="nav-link" active-class="active-tab" style="cursor:pointer">
              로그아웃
            </form>
            <RouterLink v-if="isAuthenticated" to="/mypage" class="nav-link" active-class="active-tab"
              >마이페이지
            </RouterLink>
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from "vue";

// 화면 구성 작업을 위해 임시로 만든 state 입니다.
const isAuthenticated = ref(false);
</script>

<style scoped>
.custom-navbar-bg {
  background-color: black !important;
  color: white;
  margin-bottom: 0px;
  
}
.nav-link {
  color: white;
}
.collapse navbar-collapse {
  color: white;
}
.navbar-toggle {
  color: white;
}
.active-tab {
  color: white !important;
  font-weight: bold !important;
}
</style>
