import React, { useState, useEffect } from "react";
import testService from "../api/testService";
import env from "../config/env";

const TestPage: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Record<string, unknown> | null>(null);
  const [error, setError] = useState<string | null>(null);

  const testApi = async () => {
    setLoading(true);
    setError(null);
    try {
      const result = await testService.getTest();
      setData(result);
    } catch (err: unknown) {
      if (err instanceof Error) {
        setError(err.message || "Failed to fetch data");
      } else {
        setError("Failed to fetch data");
      }
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    testApi();
  }, []);

  return (
    <div style={{ padding: "2rem", maxWidth: "800px", margin: "0 auto" }}>
      <h1 className="text-4xl font-bold text-blue-500 text-center">
        Tailwind v4 Working
      </h1>
      <h1>Backend Request Test</h1>
      
      <div style={{ marginBottom: "1rem", padding: "1rem", border: "1px solid #ccc", borderRadius: "8px" }}>
        <h3>Configuration Info:</h3>
        <p><strong>Environment:</strong> {env.mode}</p>
        <p><strong>API Base URL:</strong> {env.apiBaseUrl}</p>
      </div>

      <div style={{ marginBottom: "1rem" }}>
        <button 
          onClick={testApi} 
          disabled={loading}
          style={{ padding: "10px 20px", cursor: "pointer" }}
        >
          {loading ? "Testing..." : "Retry Request"}
        </button>
      </div>

      {loading && <p>Loading data from backend...</p>}

      {error && (
        <div style={{ color: "red", padding: "1rem", backgroundColor: "#ffebee", borderRadius: "4px" }}>
          <strong>Error:</strong> {error}
          <p style={{ fontSize: "0.8rem" }}>
            (Make sure your backend is running at {env.apiBaseUrl})
          </p>
        </div>
      )}

      {data && (
        <div style={{ marginTop: "1rem" }}>
          <h3>Response from Backend:</h3>
          <pre style={{ 
            backgroundColor: "#f5f5f5", 
            padding: "1rem", 
            borderRadius: "4px",
            overflowX: "auto",
            textAlign: "left"
          }}>
            {JSON.stringify(data, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default TestPage;
