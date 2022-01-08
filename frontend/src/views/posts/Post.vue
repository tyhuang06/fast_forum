<template>
	<div v-if="post">
		<p><strong>Title:</strong> {{ post.title }}</p>
		<p><strong>Content:</strong> {{ post.content }}</p>
		<p><strong>Author:</strong> {{ post.author.username }}</p>

		<div v-if="user.id === post.author.id">
			<p>
				<router-link
					:to="{ name: 'EditPost', params: { id: post.id } }"
					class="btn btn-primary"
					>Edit</router-link
				>
			</p>
			<p>
				<button @click="removePost()" class="btn btn-secondary">
					Delete
				</button>
			</p>
		</div>
	</div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
export default {
	name: "Post",
	props: ["id"],
	async created() {
		try {
			await this.viewPost(this.id);
		} catch (error) {
			console.error(error);
			this.$router.push("/dashboard");
		}
	},
	computed: {
		...mapGetters({ post: "statePost", user: "stateUser" }),
	},
	methods: {
		...mapActions(["viewPost", "deletePost"]),
		async removePost() {
			try {
				await this.deletePost(this.id);
				this.$router.push("/dashboard");
			} catch (error) {
				console.error(error);
			}
		},
	},
};
</script>
