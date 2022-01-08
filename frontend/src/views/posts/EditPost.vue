<template>
	<section>
		<h1>Edit Post</h1>
		<hr />
		<br />
		<PostForm :submit="submit" :form="form" />
	</section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import PostForm from "@/components/PostForm.vue";
export default {
	name: "EditPost",
	props: ["id"],
	components: {
		PostForm,
	},
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
