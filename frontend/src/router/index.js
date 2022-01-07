import Vue from "vue";
import VueRouter from "vue-router";
import store from "@/store";

import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "Home",
		component: Home,
	},
	{
		path: "/register",
		name: "Register",
		component: () => import("../views/Register.vue"),
	},
	{
		path: "/login",
		name: "Login",
		component: () => import("../views/Login.vue"),
	},
	{
		path: "/dashboard",
		name: "Dashboard",
		component: () => import("../views/Dashboard.vue"),
		meta: { requiresAuth: true },
	},
	{
		path: "/profile",
		name: "Profile",
		component: () => import("../views/Profile.vue"),
		meta: { requiresAuth: true },
	},
	{
		path: "/post/:id",
		name: "Post",
		component: () => import("../views/Post.vue"),
		meta: { requiresAuth: true },
		props: true,
	},
	{
		path: "/post/:id/edit",
		name: "EditPost",
		component: () => import("../views/EditPost.vue"),
		meta: { requiresAuth: true },
		props: true,
	},
	{
		path: "/about",
		name: "About",
		// route level code-splitting
		// this generates a separate chunk (about.[hash].js) for this route
		// which is lazy-loaded when the route is visited.
		component: () =>
			import(/* webpackChunkName: "about" */ "../views/About.vue"),
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

// Handle not authorized redirect to login
router.beforeEach((to, from, next) => {
	if (to.matched.some((record) => record.meta.requiresAuth)) {
		if (store.getters.isAuthenticated) {
			next();
			return;
		}
		next("/login");
	} else {
		next();
	}
});

export default router;
