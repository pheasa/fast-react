import React from "react";
import { useNavigate, useLocation } from "react-router-dom";
import Cookies from "js-cookie";

const LoginPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const from = location.state?.from?.pathname || "/home";

  const handleMockLogin = () => {
    // 1. Mock setting a cookie with an 'access_token' (expires in 1 hour)
    // Using js-cookie to set the token
    Cookies.set("access_token", "mock-jwt-token-from-cookie", { expires: 1/24, path: "/" });

    console.log("Mock login successful! Token saved to cookie using js-cookie. Redirecting...");
    navigate(from, { replace: true });
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", height: "100vh", padding: "1rem" }}>
      <h1>Login</h1>
      <p>Authentication is required to access the Settings page.</p>
      <button 
        onClick={handleMockLogin}
        style={{ padding: "10px 20px", fontSize: "1rem", cursor: "pointer", backgroundColor: "#3b82f6", color: "white", border: "none", borderRadius: "4px" }}
      >
        Mock Login & Continue
      </button>
      <p style={{ marginTop: "1rem", fontSize: "0.8rem", color: "#666" }}>
        In a real app, your server will verify your cookie.
      </p>
    </div>
  );
};

export default LoginPage;
