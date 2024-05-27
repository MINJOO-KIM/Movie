import { createApp } from "vue";
import { createPinia } from "pinia";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";

import App from "./App.vue";
import router from "./router";

// Bootstrap
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";
import "bootstrap/dist/js/bootstrap";

const app = createApp(App);
const pinia = createPinia();

pinia.use(piniaPluginPersistedstate);
// app.use(createPinia());
app.use(pinia);
app.use(router);

app.mount("#app");
