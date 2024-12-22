/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class', // Enable dark mode by class
  content: [
    './templates/**/*.html',
    './**/*.py',
  ],
  theme: {
    extend: {
      colors: {
        'melonx-gray': '#2c3e50',
        'melonx-red': '#e74c3c',
      },
      animation: {
        'mesh-gradient': 'mesh-gradient 8s ease infinite',
      },
      keyframes: {
        'mesh-gradient': {
          '0%, 100%': {
            backgroundPosition: '0% 50%',
          },
          '50%': {
            backgroundPosition: '100% 50%',
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('daisyui'),
    require('tailwindcss-animated'),
  ],

}
