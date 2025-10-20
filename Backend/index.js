import express from "express";
import pkg from "pg";
const { Pool } = pkg;

const app = express();

const pool = new Pool({
  user: "postgres",
  host: "db",
  database: "mydb",
  password: "postgres",
  port: 5432,
});

app.get("/", async (req, res) => {
  try {
    const result = await pool.query("SELECT NOW()");
    res.json({
      message: "Salem from Node,Postgres,Docker",
      time: result.rows[0],
    });
  } catch (err) {
    console.error(err);
    res.status(500).send("Database connection error");
  }
});

app.listen(3000, () => console.log("✅ Server running on port 3000"));
