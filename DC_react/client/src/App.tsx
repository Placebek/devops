import { useEffect, useState } from "react";

function App() {
  const [message, setMessage] = useState("Loading...");

  useEffect(() => {
    setMessage("React + Docker + PostgreSQL 🚀");
  }, []);

  return (
    <div style={{ fontFamily: "sans-serif", textAlign: "center", marginTop: "3rem" }}>
      <h1>{message}</h1>
      <p>Frontend работает на порту 3000</p>
    </div>
  );
}

export default App;
