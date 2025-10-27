# Board Games
# ---------------------------- IMPORTS ------------------------------- #
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Home page
@app.route("/")
def index():
    return render_template("index.html")

# Handle form submission
@app.route("/search", methods=["POST"])
def search():
    user_input = request.form["query"]

    with open("data.json") as f:
        data = json.load(f)

    # Get value from JSON (or "Not found")
    result = data.get(user_input, "Not found")

    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
