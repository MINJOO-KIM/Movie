<template>
  <header>
    <nav class="navbar navbar-expand-lg">
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
          <div class="navbar-nav ms-auto d-flex">
            <RouterLink to="/" class="nav-link" active-class="active-tab"
              >영화추천</RouterLink
            >
            <RouterLink
              to="/ai-recommend"
              class="nav-link"
              active-class="active-tab"
              >AI추천</RouterLink
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
</style>
