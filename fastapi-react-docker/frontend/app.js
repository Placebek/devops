import React, { useEffect, useState } from "react";
import ReactDOM from "react-dom/client";

const App = () => {
  const [message, setMessage] = useState("Жүктеліп жатыр...");

  // Backend-пен байланыс
  useEffect(() => {
    fetch("http://localhost:8000/")
      .then((res) => res.json())
      .then((data) => setMessage(data.message))
      .catch((err) => setMessage("Серверге қосыла алмады 😢"));
  }, []);

  return (
    <div style={{
      fontFamily: "sans-serif",
      textAlign: "center",
      marginTop: "100px"
    }}>
      <h1>🦄 Docker + FastAPI + React</h1>
      <h2>{message}</h2>
      <p style={{ color: "#777" }}>
        Backend → FastAPI | Frontend → React | DB → PostgreSQL
      </p>
    </div>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<App />);
