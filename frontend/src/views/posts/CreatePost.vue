<template>
	<section>
		<h1>Add new Post</h1>
		<hr />
		<br />

		<Form :submit="submit" :form="form" />
	</section>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import Form from "@/components/Form.vue";
export default {
	name: "CreatePost",
	components: {
		Form,
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
