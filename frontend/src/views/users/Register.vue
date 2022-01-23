<template>
	<section>
		<form @submit.prevent="submit">
			<div class="mb-3">
				<FormulateInput
					type="text"
					name="username"
					label="Username:"
					validation="required"
					v-model="user.username"
				/>
			</div>
			<div class="mb-3">
				<FormulateInput
					type="text"
					name="email"
					label="Email:"
					validation="required|email"
					v-model="user.email"
				/>
			</div>
			<div class="mb-3">
				<FormulateInput
					type="password"
					name="password"
					label="Password:"
					validation="required"
					v-model="user.password"
				/>
			</div>
			<FormulateInput type="submit" name="Sign Up" />
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
