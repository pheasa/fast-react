import { useState } from 'react'
import { Link } from "react-router-dom"
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { env } from './config/env'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>

      <div style={{ marginTop: "2rem", padding: "1rem", backgroundColor: "#333", borderRadius: "8px" }}>
        <h2>Architecture Test</h2>
        <p>Click below to test the connection to your backend:</p>
        <Link to="/test" style={{ color: "#646cff", fontWeight: "bold", fontSize: "1.2rem" }}>
          Go to Backend Test Page
        </Link>
      </div>

      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      <div>API Base: {env.appTitle}</div>
    </>
  )
}

export default App
