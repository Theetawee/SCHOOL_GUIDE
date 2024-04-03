/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",

  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#f0f9ff",
          100: "#E1F5FE",
          200: "#bae6fd",
          300: "#7dd3fc",
          400: "#38bdf8",
          500: "#0ea5e9",
          600: "#0284c7",
          700: "#0369a1",
          800: "#075985",
          900: "#0c4a6e",
          950: "#082f49",
        },
        gray: {
          50: "#FAFAFA",
          100: "#F5F5F5 ",
          200: "#EEEEEE",
          300: "#E0E0E0 ",
          400: "#BDBDBD ",
          500: "#9E9E9E ",
          600: "#757575 ",
          700: "#616161 ",
          800: "#424242 ",
          900: "#212121 ",
          950: "#121212",
        },
      },
    },
  },
  plugins: [require("flowbite/plugin")],
};
