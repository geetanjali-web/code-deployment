from flask import Flask, render_template, request
import json, os

app = Flask(__name__)

# Load data from JSON
with open(os.path.join(os.path.dirname(__file__), "data.json"), "r", encoding="utf-8") as f:
    data = json.load(f)

attractions_list = data.get("attractions", [])
hotels_list = data.get("hotels", [])
food_list = data.get("foods", [])

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/attractions")
def attractions():
    return render_template("attractions.html", attractions=attractions_list)

@app.route("/hotels")
def hotels():
    return render_template("hotels.html", hotels=hotels_list)

@app.route("/food")
def food():
    return render_template("food.html", foods=food_list)

@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.args.get("q", "").lower()
    results = []
    if query:
        for item in attractions_list + hotels_list + food_list:
            if query in item["name"].lower():
                results.append(item)
    return render_template("search.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
