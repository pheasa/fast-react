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

  /** define key to using in project */
  appTitle: string;
}

export const env: EnvConfig = {
  mode: import.meta.env.MODE,
  isDev: import.meta.env.DEV,
  isProd: import.meta.env.PROD,
  
  // For client-side, we must use APP_ prefix if we want them here.
  appTitle: import.meta.env.APP_TITLE,
};

export default env;
