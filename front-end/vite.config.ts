import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from "@tailwindcss/vite";

// https://vite.dev/config/
export default defineConfig({
  envPrefix: "APP_", // only variables starting with APP_ will be exposed to the client
  plugins: [react(), tailwindcss()],
  server: {
    proxy: {
      "/api": {
        target: process.env.REACT_APP_API_URL,
        changeOrigin: true,
        secure: false,
        rewrite: (path) => path.replace(/^\/api/, ""), // remove /api prefix
      },
    },
    allowedHosts: process.env.REACT_ALLOWED_HOSTS?.split(",") ?? [], // ← paste your current ngrok host
    host: true, // allow external access
  },
});
