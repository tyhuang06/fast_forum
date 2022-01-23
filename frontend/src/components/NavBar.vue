<template>
	<header>
		<div class="navbar w-full flex fixed">
			<div class="flex w-full justify-between items-center mx-16">
				<div class="nav_left flex items-center">
					<a class="flex text-2xl mr-4" href="/">Fast Forum</a>
					<ul class="flex flex-row h-full items-center">
						<li class="nav_link">
							<router-link class="" to="/">Home</router-link>
						</li>
						<li class="nav_link">
							<router-link class="" to="/dashboard"
								>Dashboard</router-link
							>
						</li>
					</ul>
				</div>
				<div class="nav_right flex items-center">
					<ul
						v-if="isLoggedIn"
						class="flex flex-row h-full items-center self-end"
					>
						<li class="nav_link">
							<router-link class="" to="/profile"
								>My Profile</router-link
							>
						</li>
						<li class="nav_link">
							<a class="" @click="logout">Log Out</a>
						</li>
					</ul>
					<ul v-else class="flex flex-row h-full items-center">
						<li class="nav_link">
							<router-link class="" to="/register"
								>Register</router-link
							>
						</li>
						<li class="nav_link">
							<router-link class="" to="/login"
								>Log In</router-link
							>
						</li>
					</ul>
				</div>
			</div>
		</div>
		<nav class="navbar navbar-expand-md navbar-dark bg-dark">
			<div class="">
				<button
					class="navbar-toggler"
					type="button"
					data-bs-toggle="collapse"
					data-bs-target="#navbarCollapse"
					aria-controls="navbarCollapse"
					aria-expanded="false"
					aria-label="Toggle navigation"
				>
					<span class="navbar-toggler-icon"></span>
				</button>
				<div class="collapse navbar-collapse" id="navbarCollapse"></div>
			</div>
		</nav>
	</header>
</template>

<script>
export default {
	name: "NavBar",
	computed: {
		isLoggedIn: function () {
			return this.$store.getters.isAuthenticated;
		},
	},
	methods: {
		async logout() {
			await this.$store.dispatch("logOut");
			this.$router.push("/login");
		},
	},
};
</script>

<style lang="postcss">
.navbar {
	@apply shadow;
	height: 60px;
}

.nav_link {
	@apply px-4 cursor-pointer;
}
</style>
