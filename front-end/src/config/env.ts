/**
 * env.ts
 *
 * Utility to safely access environment variables in a Vite project.
 * Supports both development and production environments.
 *
 * Notes:
 * - ALLOWED_HOSTS can be set in `.env` without a prefix.
 * - No need to touch `vite.config.ts`.
 * - Automatically splits comma-separated values for array use.
 * - Safe defaults provided if env variable is missing.
 */

import { loadEnv } from "vite";

interface EnvConfig {
  /** Current environment mode (development, production, etc.) */
  mode: string;

  /** Flag for development mode */
  isDev: boolean;

  /** Flag for production mode */
  isProd: boolean;

  /** List of allowed hosts (from .env ALLOWED_HOSTS) */
  allowHosts: string[];
}

// Load environment variables from .env files
// - mode: development | production
// - process.cwd(): project root
// - "" : load all variables, no prefix required
const envVars = loadEnv(import.meta.env.MODE, process.cwd(), "");

export const env: EnvConfig = {
  mode: import.meta.env.MODE,
  isDev: import.meta.env.DEV,
  isProd: import.meta.env.PROD,

  // ALLOWED_HOSTS can be comma-separated in .env
  // Defaults to empty array if not set
  allowHosts: envVars.ALLOWED_HOSTS?.split(",") ?? [],
};

export default env;
