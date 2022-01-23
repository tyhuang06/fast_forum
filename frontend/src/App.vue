<template>
	<div id="app">
		<NavBar />
		<div class="container">
			<router-view />
		</div>
	</div>
</template>

<script>
// @ is an alias to /src
import NavBar from "@/components/NavBar.vue";
export default {
	components: {
		NavBar,
	},
};
</script>

<style lang="postcss">
#app {
	@apply text-gray-900;
	font-family: Avenir, Helvetica, Arial, sans-serif;
	-webkit-font-smoothing: antialiased;
	-moz-osx-font-smoothing: grayscale;
	color: #2c3e50;
}

.container {
	@apply pt-6 px-60;
}
</style>
