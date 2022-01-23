<template>
	<section>
		<form @submit.prevent="submit">
			<div class="mb-3">
				<FormulateInput
					type="text"
					name="username"
					label="Username:"
					validation="required"
					v-model="form.username"
				/>
			</div>
			<div class="mb-3">
				<FormulateInput
					type="password"
					name="password"
					label="Password:"
					validation="required"
					v-model="form.password"
				/>
			</div>
			<FormulateInput type="submit" name="Login" />
		</form>
	</section>
</template>

<script>
import { mapActions } from "vuex";
export default {
	name: "Login",
	data() {
		return {
			form: {
				username: "",
				password: "",
			},
		};
	},
	methods: {
		...mapActions(["logIn"]),
		async submit() {
			const User = new FormData();
			User.append("username", this.form.username);
			User.append("password", this.form.password);
			await this.logIn(User);
			this.$router.push("/dashboard");
		},
	},
};
</script>
