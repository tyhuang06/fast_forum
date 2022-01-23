<template>
	<section>
		<div class="text-2xl">Create New Post</div>
		<hr />
		<br />

		<PostForm :submit="submit" :form="form" />
	</section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import PostForm from "@/components/PostForm.vue";
export default {
	name: "CreatePost",
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
	computed: {
		...mapGetters({ posts: "statePosts" }),
	},
	methods: {
		...mapActions(["createPost"]),
		async submit() {
			await this.createPost(this.form);

			this.$router.push({
				name: "Dashboard",
			});
		},
	},
};
</script>
