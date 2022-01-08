<template>
	<section>
		<h1>Edit Post</h1>
		<hr />
		<br />

		<form @submit.prevent="submit">
			<div class="mb-3">
				<label for="title" class="form-label">Title:</label>
				<input
					type="text"
					name="title"
					v-model="form.title"
					class="form-control"
				/>
			</div>
			<div class="mb-3">
				<label for="content" class="form-label">Content:</label>
				<textarea
					name="content"
					v-model="form.content"
					class="form-control"
				></textarea>
			</div>
			<button type="submit" class="btn btn-primary">Submit</button>
		</form>
	</section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
	name: "EditPost",
	props: ["id"],
	data() {
		return {
			form: {
				title: "",
				content: "",
			},
		};
	},
	created: function () {
		this.GetPost();
	},
	computed: {
		...mapGetters({ post: "statePost" }),
	},
	methods: {
		...mapActions(["updatePost", "viewPost"]),
		async submit() {
			try {
				let post = {
					id: this.id,
					form: this.form,
				};
				await this.updatePost(post);

				this.$router.push({
					name: "Post",
					params: { id: this.post.id },
				});
			} catch (error) {
				console.log(error);
			}
		},
		async GetPost() {
			try {
				await this.viewPost(this.id);
				this.form.title = this.post.title;
				this.form.content = this.post.content;
			} catch (error) {
				console.error(error);
				this.$router.push("/dashboard");
			}
		},
	},
};
</script>
