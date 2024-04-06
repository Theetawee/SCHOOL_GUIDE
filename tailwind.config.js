const plugin = require('tailwindcss/plugin');


/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: "class",

  content: ["./templates/**/*.html", "./node_modules/flowbite/**/*.js"],
  theme: {
    extend: {
      colors: {
        primary: {
          50: "#f0fdfa",
          100: "#ccfbf1",
          200: "#99f6e4",
          300: "#5eead4",
          400: "#2dd4bf",
          500: "#14b8a6",
          600: "#0d9488",
          700: "#0f766e",
          800: "#115e59",
          900: "#134e4a",
          950: "#042f2e",
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
  plugins: [require("flowbite/plugin"),

  plugin(function ({ addVariant, e, postcss }) {
	  addVariant('firefox', ({ container, separator }) => {
		const isFirefoxRule = postcss.atRule({
		  name: '-moz-document',
		  params: 'url-prefix()',
		});
		isFirefoxRule.append(container.nodes);
		container.append(isFirefoxRule);
		isFirefoxRule.walkRules((rule) => {
		  rule.selector = `.${e(
			`firefox${separator}${rule.selector.slice(1)}`
		  )}`;
		});
	  });
	}),
],
};
