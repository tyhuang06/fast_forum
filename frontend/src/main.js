import Vue from "vue";
import App from "./App.vue";

import "./index.css";
import router from "./router";
import store from "./store";
import axios from "axios";
import "./assets/tailwind.css";
import "@braid/vue-formulate/dist/snow.min.css";

import VueFormulate from "@braid/vue-formulate";

Vue.config.productionTip = false;

new Vue({
	router,
	store,
	render: (h) => h(App),
}).$mount("#app");

axios.defaults.withCredentials = true;
axios.defaults.baseURL = process.env.VUE_APP_BACKEND_API; // FastAPI backend

// Handle expired tokens
axios.interceptors.response.use(undefined, function (error) {
	if (error) {
		const originalRequest = error.config;
		if (error.response.status === 401 && !originalRequest._retry) {
			originalRequest._retry = true;
			store.dispatch("logOut");
			return router.push("/login");
		}
	}
});

Vue.use(VueFormulate);
