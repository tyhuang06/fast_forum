<template>
	<div v-if="post">
		<div class="flex flex-col">
			<div class="flex justify-between items-center">
				<div class="text-2xl font-bold">
					{{ post.title }}
				</div>
				<div class="ml-2">
					Posted by
					<span class="text-blue-700">{{
						post.author.username
					}}</span>
				</div>
			</div>
			<div class="mt-4">{{ post.content }}</div>
		</div>

		<div v-if="user.id === post.author.id" class="flex justify-end mt-4">
			<div class="flex">
				<router-link
					:to="{ name: 'EditPost', params: { id: post.id } }"
					class="button-base"
					>Edit</router-link
				>
			</div>
			<div class="flex">
				<button
					@click="removePost()"
					class="button-base bg-red-700 ml-2 hover:bg-red-500"
				>
					Delete
				</button>
			</div>
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
