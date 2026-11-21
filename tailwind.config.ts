import type { Config } from 'tailwindcss';

const config: Config = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
    './src/features/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        petrol: {
          50: '#f0f7fb',
          100: '#e0eff7',
          200: '#b9dfef',
          300: '#7dc4e3',
          400: '#3aa5d2',
          500: '#176ea9',
          600: '#125c90',
          700: '#0e4c77',
          800: '#0a3658',
          900: '#082a45',
          950: '#051b2d',
        },
        brand: {
          primary: '#0a3658',
          secondary: '#0e4c77',
          accent: '#0284c7',
          light: '#f0f5fa',
          dark: '#082a45',
        },
      },
      fontFamily: {
        cairo: ['Cairo', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
        sans: ['Cairo', 'system-ui', 'sans-serif'],
      },
      boxShadow: {
        subtle: '0 2px 10px rgba(10, 54, 88, 0.05)',
        card: '0 4px 20px rgba(10, 54, 88, 0.08)',
        hover: '0 8px 30px rgba(10, 54, 88, 0.12)',
      },
    },
  },
  plugins: [],
};

export default config;
