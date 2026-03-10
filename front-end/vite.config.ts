import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  
  return {
    plugins: [react()],
    server: {
      proxy: {
        // Only proxy /api calls to the backend
        "/api": {
          target: env.API_BASE_URL ?? "",
          changeOrigin: true,
          secure: false,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
      allowedHosts: env.ALLOWED_HOSTS ? env.ALLOWED_HOSTS.split(",") : [],
      host: true,
    },
    optimizeDeps: {
      force: true,
    },
  };
});
