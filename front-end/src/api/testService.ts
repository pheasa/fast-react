import axiosInstance from "./axiosInstance";

export const testService = {
  getTest: async () => {
    const response = await axiosInstance.get("/");
    return response.data;
  },
  
  // Example for a real endpoint (e.g., users)
  getUsers: async () => {
    const response = await axiosInstance.get("/users");
    return response.data;
  }
};

export default testService;
