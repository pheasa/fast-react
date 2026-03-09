import { defineConfig, loadEnv } from 'vite'

// https://vite.dev/config/
export default defineConfig(({ mode }) => {
  const env = loadEnv(mode, process.cwd(), "");
  
  return {
    enableReactRefresh: false, // Disable React Fast Refresh for better ngrok compatibility
    server: {
      proxy: {
        "/api": {
          target: env.API_URL,
          changeOrigin: true,
          secure: false,
          rewrite: (path) => path.replace(/^\/api/, ""), // remove /api prefix
        },
      },
      allowedHosts: env.ALLOWED_HOSTS?.split(",") ?? [], // ← paste your current ngrok host
      host: true, // allow external access
    },
  };
});