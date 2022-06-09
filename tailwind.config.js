module.exports = {
    content: [
        './app/templates/**/*.{html,js}',
        './node_modules/flowbite/**/*.js',
    ],
    theme: {
        extend: {},
    },
    plugins: [require('flowbite/plugin')],
};
