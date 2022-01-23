<template>
	<section>
		<div class="text-2xl">Profile</div>
		<hr />
		<br />

		<div class="flex flex-col">
			<div class="flex justify-between">
				<div class="flex">
					<img :src="this.profile_url" alt="" />
				</div>
				<div class="flex flex-col pl-4">
					<div class="mb-2">New Profile Picture</div>
					<form
						@submit.prevent="uploadFile"
						enctype="multipart/form-data"
					>
						<input
							ref="file"
							type="file"
							id="file"
							@change="handleFileUpload()"
						/>
						<button
							type="submit"
							class="button-base bg-green-600 hover:bg-green-500 mt-2"
						>
							Upload Picture
						</button>
					</form>
				</div>
			</div>
			<div class="mt-4 text-xl">
				<div>
					<strong>Username:</strong> <span>{{ user.username }}</span>
				</div>
				<div>
					<strong>Email:</strong> <span>{{ user.email }}</span>
				</div>
			</div>
			<br />
			<hr />
			<div class="flex mt-4">
				<div class="flex">
					<router-link
						:to="{ name: 'ProfileUpdate' }"
						class="button-base"
						>Edit</router-link
					>
				</div>
				<div>
					<button
						@click="deleteAccount()"
						class="button-base bg-red-700 ml-2 hover:bg-red-500"
					>
						Delete Account
					</button>
				</div>
			</div>
		</div>
	</section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
	name: "Profile",
	data() {
		return {
			file: "",
		};
	},
	created: function () {
		return this.$store.dispatch("viewAccount");
	},
	computed: {
		...mapGetters({ user: "stateUser" }),
		profile_url: function () {
			let url =
				process.env.VUE_APP_BACKEND_API +
				"static/images/" +
				this.user.profile_pic;
			return url;
		},
	},
	methods: {
		...mapActions(["deleteUser", "uploadProfile"]),
		async deleteAccount() {
			try {
				await this.deleteUser(this.user.id);
				await this.$store.dispatch("logOut");
				this.$router.push("/");
			} catch (error) {
				console.error(error);
			}
		},
		async uploadFile() {
			try {
				let formData = new FormData();
				formData.append("file", this.file);
				console.log(formData);
				await this.uploadProfile(formData);

				this.$router.go({
					name: "Profile",
				});
			} catch (error) {
				console.log(error);
			}
		},
		handleFileUpload() {
			this.file = this.$refs.file.files[0];
			console.log(this.file);
		},
	},
};
</script>
