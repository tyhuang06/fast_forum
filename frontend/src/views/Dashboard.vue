<template>
	<div>
		<section>
			<h1>Add new Post</h1>
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

		<br /><br />

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
import { mapGetters, mapActions } from "vuex";
export default {
	name: "Dashboard",
	data() {
		return {
			form: {
				title: "",
				content: "",
			},
		};
	},
	created: function () {
		return this.$store.dispatch("getPosts");
	},
	computed: {
		...mapGetters({ posts: "statePosts" }),
	},
	methods: {
		...mapActions(["createPost"]),
		async submit() {
			await this.createPost(this.form);
		},
	},
};
</script>
