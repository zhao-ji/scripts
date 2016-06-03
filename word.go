package main

import (
	"flag"
	"fmt"
	"github.com/garyburd/redigo/redis"
	"log"
	"net/http"
	"time"
)

var addr = flag.String("addr", "127.0.0.1:1111", "http service address")

func main() {
	flag.Parse()
	http.Handle("/", http.HandlerFunc(word))
	err := http.ListenAndServe(*addr, nil)
	if err != nil {
		log.Fatal("Listen and Serve: ", err)
	}
}

func word(w http.ResponseWriter, req *http.Request) {
	word := req.FormValue("word")

	connect, err := redis.Dial("tcp", ":6379")
	if err != nil {
		log.Fatal("redis connect error: ", err)
	}
	defer connect.Close()

	connect.Do("SELECT", 15)
	connect.Do("INCR", word)
	now := time.Now()
	connect.Do("SELECT", 14)
	connect.Do("SET", now.Format("060102150405"), word)
	fmt.Fprintf(w, "")
}
