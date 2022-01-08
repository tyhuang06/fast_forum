import Vue from "vue";
import App from "./App.vue";

import router from "./router";
import store from "./store";
import axios from "axios";

axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/"; // FastAPI backend

Vue.config.productionTip = false;

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

new Vue({
	router,
	store,
	render: (h) => h(App),
}).$mount("#app");
