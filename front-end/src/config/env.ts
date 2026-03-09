/**
 * env.ts
 *
 * Utility to safely access environment variables in a Vite project.
 * Supports both development and production environments.
 */

interface EnvConfig {
  /** Current environment mode (development, production, etc.) */
  mode: string;

  /** Flag for development mode */
  isDev: boolean;

  /** Flag for production mode */
  isProd: boolean;

  /** API Base URL */
  apiBaseUrl: string;

  /** List of allowed hosts (from .env ALLOWED_HOSTS) */
  allowHosts: string[];
}

export const env: EnvConfig = {
  mode: import.meta.env.MODE,
  isDev: import.meta.env.DEV,
  isProd: import.meta.env.PROD,
  
  // Use /api to benefit from the Vite proxy setup
  apiBaseUrl: import.meta.env.VITE_API_BASE_URL,

  // For client-side, we must use VITE_ prefix if we want them here, 
  // or they must be exported by Vite via import.meta.env
  allowHosts: (import.meta.env.VITE_ALLOWED_HOSTS as string)?.split(","),
};

export default env;
