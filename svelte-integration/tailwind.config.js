/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				primary: {
					400: '#E3F5FF'
				},
				secondary: {
					300: '#F7F9FB',
					400: '#E5ECF6',
					500: '#b6c4cc'
				},
				accent: {
					300: '#333333',
					400: '#1C1C1C'
				}
			}
		}
	},
	plugins: []
};
