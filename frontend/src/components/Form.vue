<template>
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
</template>

<script>
export default {
	name: "Form",
	props: ["form", "submit"],
};
</script>
