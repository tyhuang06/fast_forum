<template>
	<div>
		<p>
			<router-link :to="{ name: 'CreatePost' }" class="btn btn-primary"
				>New Post</router-link
			>
		</p>
		<section>
			<h1>Posts</h1>
			<hr />
			<br />

			<div v-if="posts.length">
				<div v-for="post in posts" :key="post.id" class="posts">
					<div class="card" style="width: 18rem">
						<div class="card-body">
							<ul>
								<li>
									<strong>Note Title:</strong>
									{{ post.title }}
								</li>
								<li>
									<strong>Author:</strong>
									{{ post.author.username }}
								</li>
								<li>
									<router-link
										:to="{
											name: 'Post',
											params: { id: post.id },
										}"
										>View</router-link
									>
								</li>
							</ul>
						</div>
					</div>
					<br />
				</div>
			</div>

			<div v-else>
				<p>Nothing to see. Check back later.</p>
			</div>
		</section>
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
