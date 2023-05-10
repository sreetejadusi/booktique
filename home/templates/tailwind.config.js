/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./**/*.{html,js}"],
  theme: {
    extend: {
      fontFamily: {
        'lemonade': ['Lemonade'],
        'montserrat': ['Montserrat']
      },
      colors: {
        'theme':'#FF725D'
      }
    },
  },
  plugins: [],
}

