<template>
	<section>
		<form @submit.prevent="submit">
			<div class="mb-3">
				<label for="username" class="form-label">Username:</label>
				<input
					type="text"
					name="username"
					v-model="user.username"
					class="form-control"
				/>
			</div>
			<div class="mb-3">
				<label for="email" class="form-label">Email:</label>
				<input
					type="text"
					name="email"
					v-model="user.email"
					class="form-control"
				/>
			</div>
			<div class="mb-3">
				<label for="password" class="form-label">Password:</label>
				<input
					type="password"
					name="password"
					v-model="user.password"
					class="form-control"
				/>
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
		</form>
	</section>
</template>

<script>
import { mapActions } from "vuex";
export default {
	name: "Register",
	data() {
		return {
			user: {
				username: "",
				email: "",
				password: "",
			},
		};
	},
	methods: {
		...mapActions(["register"]),
		async submit() {
			try {
				await this.register(this.user);
				this.$router.push("/dashboard");
			} catch (error) {
				throw "Username already exists. Please try again.";
			}
		},
	},
};
</script>
