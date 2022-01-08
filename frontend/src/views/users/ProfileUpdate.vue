<template>
	<section>
		<h1>Edit Account</h1>
		<hr />
		<br />

		<FormulateForm @submit="submit">
			<div class="mb-3">
				<FormulateInput
					type="password"
					name="password"
					label="Password:"
					validation="required"
					v-model="user.password"
				/>
			</div>
			<div class="mb-3">
				<FormulateInput
					label="Confirm password"
					type="password"
					name="password_confirm"
					validation="required|confirm"
					validation-name="Password confirmation"
				/>
			</div>
			<FormulateInput type="submit" name="Confirm" />
		</FormulateForm>
	</section>
</template>

<script>
import { mapActions } from "vuex";
export default {
	name: "Profile",
	data() {
		return {
			file: "",
			user: {
				password: "",
			},
		};
	},
	created: function () {},
	methods: {
		...mapActions(["updateUser"]),
		async submit() {
			try {
				await this.updateUser(this.user);

				this.$router.push({
					name: "Profile",
				});
			} catch (error) {
				console.log(error);
			}
		},
	},
};
</script>
