<template>
    <div class="login-container">
        <form class="login-form">
            <h2>로그인</h2>
            <div class="input-container">
                <p>
                    <input type="text" placeholder="아이디">
                </p>
                <p>
                    <input type="text" placeholder="비밀번호">
                </p>
                <button type="submit">로그인</button>
            </div>
        </form>
    </div>
</template>

<script setup>
</script>

<style scoped>
.login-container {
    display: flex;
    justify-content: center;
    align-items: center;

    height: 90vh;
}

.login-form {
    text-align: center;
}

.input-container {
    width: 440px;
}

.input-container * {
    width: 100%;
    height: 50px;
}

.login-form  button {
    color: #AAAAAA;
    margin-top: 60px;

    background-color: #424242;
    border: 1px solid white;
    border-radius: 10px;

    opacity: 85%;

    /* hover 시 black */
}

.login-form button:hover {
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
    color: #AAAAAA;
}
</style>