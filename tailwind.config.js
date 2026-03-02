/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
    content: [
        "./characters/templates/**/*.html",
    ],
    theme: {
        extend: {
            colors: {
                primary: "#a855f7",
                "primary-glow": "#c084fc",
                "background-dark": "#050608",
                "glass-border": "rgba(255, 255, 255, 0.08)",
                "glass-bg": "rgba(15, 17, 21, 0.35)",
                "neon-purple": "#a855f7",
                "neon-pink": "#ec4899",
                "neon-blue": "#3b82f6",
                "neon-cyan": "#06b6d4",
                "neon-green": "#22c55e",
            },
            fontFamily: {
                sans: ["Outfit", "sans-serif"],
            },
            borderRadius: {
                DEFAULT: "0.75rem",
                xl: "1rem",
                '2xl': "1.5rem",
                '3xl': "2rem",
            },
            boxShadow: {
                'neon-purple': '0 0 10px rgba(168, 85, 247, 0.3), 0 0 20px rgba(168, 85, 247, 0.1)',
                'neon-blue': '0 0 10px rgba(59, 130, 246, 0.3), 0 0 20px rgba(59, 130, 246, 0.1)',
                'neon-green': '0 0 10px rgba(34, 197, 94, 0.3), 0 0 20px rgba(34, 197, 94, 0.1)',
            },
            animation: {
                'pulse-slow': 'pulse 6s cubic-bezier(0.4, 0, 0.6, 1) infinite',
                'float': 'float 8s ease-in-out infinite',
                'float-delayed': 'float 9s ease-in-out 1s infinite',
                'orb-move': 'orb-move 20s infinite alternate',
                'shimmer': 'shimmer 2.5s infinite linear',
            },
            keyframes: {
                float: {
                    '0%, 100%': { transform: 'translateY(0)' },
                    '50%': { transform: 'translateY(-15px)' },
                },
                'orb-move': {
                    '0%': { transform: 'translate(0, 0) scale(1)' },
                    '33%': { transform: 'translate(50px, -30px) scale(1.1)' },
                    '66%': { transform: 'translate(-30px, 40px) scale(0.95)' },
                    '100%': { transform: 'translate(20px, -20px) scale(1.05)' },
                },
                shimmer: {
                    '0%': { backgroundPosition: '-1000px 0' },
                    '100%': { backgroundPosition: '1000px 0' },
                },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
    ],
};
