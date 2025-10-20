package main

import (
	"context"
	"fmt"
	"log"
	"net/http"
	"os"

	"github.com/jackc/pgx/v5/pgxpool"
)

func main() {
	databaseUrl := os.Getenv("DATABASE_URL")
	pool, err := pgxpool.New(context.Background(), databaseUrl)
	if err != nil {
		log.Fatal("Unable to connect to DB:", err)
	}
	defer pool.Close()

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello World from Go, Ml engineer Darkhan!")
	})

	fmt.Println("Server running on port 8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
