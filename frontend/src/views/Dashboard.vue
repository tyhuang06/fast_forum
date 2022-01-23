<template>
	<div class="flex flex-col">
		<div class="flex mb-4">
			<router-link :to="{ name: 'CreatePost' }" class="button-base"
				>Create New Post</router-link
			>
		</div>
		<div class="flex flex-col">
			<div v-if="posts.length">
				<div v-for="post in posts" :key="post.id" class="posts my-4">
					<div class="flex flex-col border-2 rounded-md p-2">
						<div class="flex justify-between">
							<div class="text-xl font-bold">
								{{ post.title }}
							</div>
							<div class="ml-2">
								Posted by
								<span class="text-blue-700">{{
									post.author.username
								}}</span>
							</div>
						</div>
						<div>
							<router-link
								:to="{
									name: 'Post',
									params: { id: post.id },
								}"
								class="border-b text-gray-400 hover:text-gray-700 hover:border-gray-700"
								>View Post</router-link
							>
						</div>
					</div>
				</div>
			</div>

			<div v-else>
				<p>Nothing to see. Check back later.</p>
			</div>
		</div>
	</div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
	name: "Dashboard",

	created: function () {
		return this.$store.dispatch("getPosts");
	},
	computed: {
		...mapGetters({ posts: "statePosts" }),
	},
};
</script>
