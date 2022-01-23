<template>
	<section class="text-lg">
		<div>This is a forum site built with FastAPI and Vue.</div>

		<div>
			<a href="/dashboard" class="text-blue-700">Click here</a> to view
			all posts.
		</div>
		<div>
			<a
				href="https://github.com/tyhuang06/fast_forum"
				class="text-blue-700"
				>Click here</a
			>
			to view Github repo.
		</div>

		<div v-if="!isLoggedIn">
			<span><a href="/register">Register</a></span>
			<span> or </span>
			<span><a href="/login">Log In</a></span>
		</div>
	</section>
</template>

<script>
export default {
	name: "Home",
	computed: {
		isLoggedIn: function () {
			return this.$store.getters.isAuthenticated;
		},
	},
};
</script>
