import axiosInstance from "./axiosInstance";
import Cookies from "js-cookie";

export const authService = {
  /**
   * Verifies the authentication token by extracting it from cookies using js-cookie
   * and sending it in the Authorization header.
   */
  verifyToken: async () => {
    // 1. Get the token from cookies (assuming the cookie name is 'access_token')
    const token = Cookies.get("access_token");

    // 2. Prepare the headers
    const config = {
      headers: {
        ...(token ? { Authorization: `Bearer ${token}` } : {}),
      },
    };

    // 3. Make the verification call
    const response = await axiosInstance.get("/auth/verify", config);
    return response.data;
  },
};

export default authService;
