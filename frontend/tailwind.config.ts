import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        orbitron: ["var(--font-orbitron)", "Orbitron", "monospace"],
        inter:    ["var(--font-inter)", "Inter", "sans-serif"],
      },
      colors: {
        brand: {
          red:    "#FF4655",
          purple: "#8B5CF6",
          bg:     "#0A0E17",
          card:   "#0D1117",
        },
      },
      animation: {
        "glow-red":    "glow-red 3s ease-in-out infinite",
        "glow-purple": "glow-purple 3s ease-in-out infinite",
        "fade-up":     "fade-up 0.5s ease-out forwards",
        "spin-slow":   "spin 2s linear infinite",
        "pulse-bar":   "pulse-bar 2s ease-in-out infinite",
      },
      keyframes: {
        "glow-red": {
          "0%,100%": { boxShadow: "0 0 20px rgba(255,70,85,0.3), 0 0 60px rgba(255,70,85,0.1)" },
          "50%":     { boxShadow: "0 0 40px rgba(255,70,85,0.5), 0 0 100px rgba(255,70,85,0.15)" },
        },
        "glow-purple": {
          "0%,100%": { boxShadow: "0 0 20px rgba(139,92,246,0.3), 0 0 60px rgba(139,92,246,0.1)" },
          "50%":     { boxShadow: "0 0 40px rgba(139,92,246,0.5), 0 0 100px rgba(139,92,246,0.15)" },
        },
        "fade-up": {
          from: { opacity: "0", transform: "translateY(20px)" },
          to:   { opacity: "1", transform: "translateY(0)" },
        },
        "pulse-bar": {
          "0%":   { width: "5%" },
          "50%":  { width: "80%" },
          "100%": { width: "5%" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
