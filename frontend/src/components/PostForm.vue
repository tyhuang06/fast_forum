<template>
	<form @submit.prevent="submit">
		<div class="mb-3">
			<FormulateInput
				type="text"
				name="title"
				label="Title:"
				validation="required"
				v-model="form.title"
			/>
		</div>
		<div class="mb-3">
			<FormulateInput
				type="textarea"
				name="content"
				label="Content:"
				validation="required"
				v-model="form.content"
			/>
		</div>
		<FormulateInput type="submit" name="Submit" />
	</form>
</template>

<script>
export default {
	name: "Form",
	props: ["form", "submit"],
};
</script>
