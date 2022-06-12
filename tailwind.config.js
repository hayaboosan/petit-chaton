module.exports = {
    content: [
        './app/templates/**/*.{html,js}',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {
            fontFamily: {
                petitEn: ['EB Garamond', 'serif'],
                petitJa: ['Noto Serif JP', 'serif'],
            },
        },
    },
    plugins: [
        require('flowbite/plugin'),
        require('prettier-plugin-tailwindcss'),
    ],
    tailwindConfig: './styles/tailwind.config.js',
};
