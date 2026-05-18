# 📘 Flask + Redis Books API Documentation

This document describes a REST API built using Flask and Redis for loading, caching, and serving book data from a CSV file.

It uses:

* Flask web framework
* Redis in-memory database
* CSV data source

---

# 🚀 Overview

This application performs the following:

* Loads `books.csv` into Redis on startup
* Caches the dataset as a JSON string
* Provides paginated API to access books
* Serves additional JSON data from file

---

# ⚙️ Prerequisites

Ensure the following are installed:

* Python 3.8+
* Redis server running (WSL Ubuntu supported)
* Flask
* redis-py client

---

# 📦 Install Dependencies

```bash
pip install flask redis
```

---

# 🧠 Redis Setup (WSL Ubuntu)

Start Redis server:

```bash
sudo service redis-server start
```

Check status:

```bash
sudo service redis-server status
```

Test Redis connection:

```bash
redis-cli ping
```

Expected output:

```text
PONG
```

---

# 🏗️ Architecture

```
CSV File (books.csv)
        ↓
load_csv_to_redis()
        ↓
Redis Cache (books_data)
        ↓
Flask API
        ↓
Client (Browser / Postman)
```

---

# 🔌 Redis Connection

```python
import redis

r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)
```

* Connects to local Redis instance
* Stores cached dataset as JSON string

---

# 📥 CSV Loading Process

Function: `load_csv_to_redis()`

### Steps:

1. Check if data exists in Redis
2. If not, read CSV file
3. Convert rows into dictionaries
4. Store in Redis key `books_data`

### Redis Key:

```
books_data
```

---

# 🌐 API Endpoints

---

## 1. Get Books (Paginated)

### Endpoint:

```
GET /books
```

### Query Parameters:

| Parameter | Type | Default | Description       |
| --------- | ---- | ------- | ----------------- |
| offset    | int  | 0       | Starting index    |
| limit     | int  | 10      | Number of records |

---

### Example Request:

```
/books?offset=0&limit=5
```

---

### Example Response:

```json
{
  "offset": 0,
  "limit": 5,
  "total": 271360,
  "count": 5,
  "books": [
    {
      "ISBN": "0195153448",
      "Book-Title": "Classical Mythology",
      "Book-Author": "Mark P. O. Morford",
      "Year-Of-Publication": "2002"
    }
  ]
}
```

---

## 2. Get JSON File Data

### Endpoint:

```
GET /data
```

### Description:

Returns content of `data.json` file.

---

# 🔄 Application Flow

```
Start Application
        ↓
Connect Redis
        ↓
Load CSV into Redis (if not exists)
        ↓
Start Flask Server
        ↓
Serve API Requests
```

---

# ⚡ Performance Benefits

* Avoids repeated CSV file reads
* Uses Redis in-memory caching
* Fast pagination using Python slicing

---

# ⚠️ Important Notes

* Redis must be running before starting Flask
* CSV uses `latin-1` encoding and `;` delimiter
* Data is loaded once into Redis on startup

---

# 🧪 Testing Examples

### First 5 books

```
http://127.0.0.1:5000/books?offset=0&limit=5
```

### Next 5 books

```
http://127.0.0.1:5000/books?offset=5&limit=5
```

---

# 🏁 Summary

This project demonstrates:

* Flask REST API design
* Redis caching strategy
* CSV data processing
* Pagination using offset & limit
* High-performance in-memory data access
