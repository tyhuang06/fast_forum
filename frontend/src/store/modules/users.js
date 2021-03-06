import axios from "axios";

const state = {
	user: null,
};

const getters = {
	isAuthenticated: (state) => !!state.user,
	stateUser: (state) => state.user,
};

const actions = {
	async register({ dispatch }, form) {
		await axios.post("register", form);
		let UserForm = new FormData();
		UserForm.append("username", form.username);
		UserForm.append("password", form.password);
		await dispatch("logIn", UserForm);
	},
	async logIn({ dispatch }, user) {
		await axios.post("login", user);
		await dispatch("viewAccount");
	},
	async viewAccount({ commit }) {
		let { data } = await axios.get("user/account");
		await commit("setUser", data);
	},
	// eslint-disable-next-line no-empty-pattern
	async updateUser({}, form) {
		await axios.patch("user/account/edit", form);
	},
	// eslint-disable-next-line no-empty-pattern
	async uploadProfile({}, form) {
		await axios.post("user/account/upload", form, {
			headers: {
				"Content-Type": "multipart/form-data",
			},
		});
	},
	// eslint-disable-next-line no-empty-pattern
	async deleteUser({}, id) {
		await axios.delete(`user/${id}/delete`);
	},
	async logOut({ commit }) {
		let user = null;
		commit("logout", user);
	},
};

const mutations = {
	setUser(state, username) {
		state.user = username;
	},
	logout(state, user) {
		state.user = user;
	},
};

export default {
	state,
	getters,
	actions,
	mutations,
};
