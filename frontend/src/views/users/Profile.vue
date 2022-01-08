<template>
	<section>
		<h1>Your Profile</h1>
		<hr />
		<br />
		<div>
			<div>
				<img :src="this.profile_url" alt="" />
			</div>
			<p>
				<strong>Username:</strong> <span>{{ user.username }}</span>
			</p>
			<p>
				<strong>Email:</strong> <span>{{ user.email }}</span>
			</p>
			<p>
				<button @click="deleteAccount()" class="btn btn-primary">
					Delete Account
				</button>
			</p>
		</div>
		<div>
			<form @submit.prevent="upload_file" enctype="multipart/form-data">
				<input
					ref="file"
					type="file"
					id="file"
					@change="handleFileUpload()"
				/>
				<button type="submit">Upload</button>
			</form>
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
		async upload_file() {
			try {
				let formData = new FormData();
				formData.append("file", this.file);
				console.log(formData);
				await this.uploadProfile(formData);

				this.$router.push({
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
