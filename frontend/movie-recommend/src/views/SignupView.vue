<template>
    <div class="signup-container">
      <form class="signup-form" @submit.prevent="signUp">
        <h2>회원가입</h2>
        <div class="input-container">
          <p>
            <input
              type="text"
              placeholder="아이디"
              id="username"
              v-model.trim="username"
            />
          </p>
          <p>
            <input
              type="text"
              placeholder="비밀번호"
              id="password1"
              v-model.trim="password1"
            />
          </p>
          <button type="submit">가입하기</button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
    import { ref } from "vue";
    import { useMovieStore } from "@/stores/movie";
    
    const username = ref(null);
    const password1 = ref(null);
    const store = useMovieStore();
    
    const signUp = function () {
        const payload = {
            username: username.value,
            password1: password1.value,
        }
        store.signUp(payload)
    }
  </script>
  
  <style scoped>
  .signup-container {
    display: flex;
    justify-content: center;
    align-items: center;
  
    height: 90vh;
  }
  
  .signup-form {
    text-align: center;
  }
  
  .input-container {
    width: 440px;
  }
  
  .input-container * {
    width: 100%;
    height: 50px;
  }
  
  .signup-form button {
    color: #aaaaaa;
    margin-top: 60px;
  
    background-color: #424242;
    border: 1px solid white;
    border-radius: 10px;
  
    opacity: 85%;
  
    /* hover 시 black */
  }
  
  .signup-form button:hover {
    color: white;
    background-color: black;
  }
  
  h2 {
    margin-bottom: 45px;
  }
  
  .input-container input {
    background-color: black;
  
    border: 1px solid white;
    padding: 10px;
    border-radius: 10px;
  }
  
  .input-container input::placeholder {
    color: #aaaaaa;
  }
  </style>