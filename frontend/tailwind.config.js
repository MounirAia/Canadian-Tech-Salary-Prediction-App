/** @type {import('tailwindcss').Config} */
module.exports = {
  // path of the file for the content to analyse to generate the classes that I use
  content: ["./dist/**/*.{html,js}"],
  theme: {
    extend: {
      colors: {
        primary: {
          300: "#F7F9FB",
          400: "#E3F5FF",
        },
        secondary: {
          400: "#E5ECF6",
        },
        accent: {
          300: "#333333",
          400: "#1C1C1C",
        },
      },
    },
  },
  plugins: [],
};
