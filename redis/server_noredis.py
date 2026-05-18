from flask import Flask, jsonify, request
import json
import csv

app = Flask(__name__)

# Prevent Flask JSON sorting issue
app.json.sort_keys = False


@app.route("/data")
def get_json():
    with open("data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


@app.route("/books")
def csv_to_json():

    # Query parameters
    offset = request.args.get("offset", default=0, type=int)
    limit = request.args.get("limit", default=10, type=int)

    data = []

    with open("books.csv", newline="", encoding="latin-1") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')

        for row in reader:
            clean_row = {k: v for k, v in row.items() if k is not None}
            data.append(clean_row)

    # Pagination
    paginated_data = data[offset:offset + limit]

    return jsonify({
        "offset": offset,
        "limit": limit,
        "total": len(data),
        "count": len(paginated_data),
        "books": paginated_data
    })


if __name__ == "__main__":
    print("http://127.0.0.1:5000/books")
    print("http://127.0.0.1:5000/books?offset=0&limit=5")
    print("http://127.0.0.1:5000/books?offset=5&limit=5")
    print("http://127.0.0.1:5000/data")

    app.run(debug=True)
