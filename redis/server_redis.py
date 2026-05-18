# Start Redis inside Ubuntu WSL /opt/redis
# sudo service redis-server start


from flask import Flask, jsonify, request
import json
import csv
import redis

app = Flask(__name__)
app.json.sort_keys = False

# Redis connection
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

CSV_FILE = "books.csv"
REDIS_KEY = "books_data"


def load_csv_to_redis():

    # Skip loading if already cached
    if r.exists(REDIS_KEY):
        print("Books already loaded in Redis")
        return

    print("Loading CSV into Redis...")

    data = []

    with open(CSV_FILE, newline="", encoding="latin-1") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            clean_row = {k: v for k, v in row.items() if k is not None}
            data.append(clean_row)

    # Store entire dataset as JSON string
    r.set(REDIS_KEY, json.dumps(data))

    print("CSV loaded into Redis")


@app.route("/books")
def get_books():

    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=10, type=int)

    # Read from Redis
    cached_data = r.get(REDIS_KEY)

    if not cached_data:
        return jsonify({"error": "No data in Redis"}), 500

    data = json.loads(cached_data)

    paginated_data = data[offset:offset + limit]

    return jsonify({
        "offset": offset,
        "limit": limit,
        "total": len(data),
        "count": len(paginated_data),
        "books": paginated_data
    })


@app.route("/data")
def get_json():

    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


if __name__ == "__main__":

    # Load CSV once
    load_csv_to_redis()

    print("http://127.0.0.1:5000/books")
    print("http://127.0.0.1:5000/books?offset=0&limit=5")

    app.run(debug=True)
