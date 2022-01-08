module.exports = {
	purge: ["./public/**/*.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
	darkMode: false, // or 'media' or 'class'
	theme: {
		container: {
			center: true,
		},
		extend: {
			colors: {
				"regal-blue": "#243c5a",
			},
		},
	},
	variants: {
		extend: {},
	},
	plugins: [],
};
