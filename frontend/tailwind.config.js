module.exports = {
	purge: ["./public/**/*.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	darkMode: false, // or 'media' or 'class'
	theme: {
		container: {
			center: true,
		},
		extend: {
			colors: {
				"vue-green": "#41b883",
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
