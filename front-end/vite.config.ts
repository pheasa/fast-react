import { defineConfig, loadEnv } from 'vite'
import react from '@vitejs/plugin-react'



export default defineConfig(({ mode }) => {
  const envPrefix = "APP_";
  const env = loadEnv(mode, process.cwd(), envPrefix);
  
  return {
    envPrefix: envPrefix,
    plugins: [react()],
    server: {
      proxy: {
        // Only proxy /api calls to the backend
        "/api": {
          target: env.APP_API_BASE_URL ?? "",
          changeOrigin: true,
          secure: false,
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
      allowedHosts: env.APP_ALLOWED_HOSTS
        ? env.APP_ALLOWED_HOSTS.split(",")
        : [],
      host: true,
    },
    optimizeDeps: {
      force: true,
    },
  };
});
