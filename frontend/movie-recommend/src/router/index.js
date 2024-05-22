import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "HomeView",
      component: HomeView,
    },
    {
      path: "/:movie_id",
      name: "MovieDetailView",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/MovieDetailView.vue"),
    },
    {
      path: "/ai-recommend",
      name: "AIRecommendView",
      component: () => import("../views/AIRecommendView.vue"),
    },
    {
      path: "/otts",
      name: "OTTHomeView",
      component: () => import("../views/OTTHomeView.vue"),
    },
    {
      path: "/party-create",
      name: "PartyCreateView",
      component: () => import("../views/PartyCreateView.vue"),
    },
    {
      path: "/party-join",
      name: "PartyJoinView",
      component: () => import("../views/PartyJoinView.vue"),
    },
    {
      path: "/mypage",
      name: "MyPageView",
      component: () => import("../views/MyPageView.vue"),
    },
    {
      path: "/login",
      name: "LoginView",
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/signup",
      name: "SignupView",
      component: () => import("../views/SignupView.vue"),
    }
  ],
});

export default router;
