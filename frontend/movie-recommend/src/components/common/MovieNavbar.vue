<template>
  <header>
    <nav class="navbar navbar-expand-lg custom-navbar-bg" data-bs-theme="dark">
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
            <RouterLink to="/" class="nav-link" active-class="active-tab"
              >영화 추천</RouterLink
            >
            <RouterLink
              to="/ai-recommend"
              class="nav-link"
              active-class="active-tab"
              >AI 추천</RouterLink
            >
            <RouterLink to="/otts" class="nav-link" active-class="active-tab"
              >OTT 공유</RouterLink
            >
          </div>
        </div>
      </div>
    </nav>
  </header>
</template>

<script setup>
import { ref } from "vue";
</script>

<style scoped>
nav {
  border: 0.3px solid white;
}
.custom-navbar-bg {
  background-color: black !important;
  color: white;
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
