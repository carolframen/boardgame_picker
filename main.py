# Board Game Picker
# ---------------------------- IMPORTS ------------------------------- #
from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# ---------------------------- HOME PAGE ------------------------------- #
# Show Home Page
@app.route("/")
def index():
    return render_template("index.html")

# ---------------------------- ADD NEW GAME ------------------------------- #
# Show Add Game Page
@app.route("/add")
def add_game_page():
    return render_template("add_game.html")
# ---------------------------- SHOW GAME LIST ------------------------------- #
# Show List Games Page
@app.route("/list")
def list_games():
    return render_template("list_games.html")

# ---------------------------- FILTER GAMES ------------------------------- #
# Show Filter Games Page
@app.route("/filter")
def list_games():
    return render_template("filter_games.html")

# ---------------------------- PICK A RANDOM GAME ------------------------------- #
# Show Pick Random Game Page
@app.route("/random")
def list_games():
    return render_template("random_game.html")

# ---------------------------------------------------------- #
if __name__ == "__main__":
    app.run(debug=True)
