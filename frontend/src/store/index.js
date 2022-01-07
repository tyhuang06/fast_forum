import createPersistedState from "vuex-persistedstate";
import Vue from "vue";
import Vuex from "vuex";

import posts from "./modules/posts";
import users from "./modules/users";

Vue.use(Vuex);

export default new Vuex.Store({
	modules: {
		posts,
		users,
	},
	plugins: [createPersistedState()],
});
