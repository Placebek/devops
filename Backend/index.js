import express from "express";
import pkg from "pg";
const { Pool } = pkg;

const app = express();
const port = 3000;

const pool = new Pool({
  host: process.env.DB_HOST || "localhost",
  user: process.env.DB_USER || "postgres",
  password: process.env.DB_PASSWORD || "postgres",
  database: process.env.DB_NAME || "mydb",
});

app.get("/", async (req, res) => {
  try {
    const result = await pool.query("SELECT NOW()");
    res.send(`PostgreSQL работает! Время: ${result.rows[0].now}`);
  } catch (err) {
    console.error(err);
    res.status(500).send("Ошибка подключения к PostgreSQL");
  }
});

app.listen(port, () => {
  console.log(`Сервер запущен на http://localhost:${port}`);
});
