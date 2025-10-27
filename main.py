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
@app.route("/add", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        # Get data from the form
        name = request.form.get("gname")
        min_players = int(request.form.get("minplayers"))
        max_players = int(request.form.get("maxplayers"))
        categories = request.form.getlist("category")  # list of selected checkboxes

        # Read existing data safely
        try:
            with open("data.json", "r") as f:
                content = f.read().strip()
                if content:
                    games = json.loads(content)
                else:
                    games = []
        except FileNotFoundError:
            games = []

        # Add new game
        games.append({
            "name": name,
            "min_players": min_players,
            "max_players": max_players,
            "tags": categories
        })

        # Write back to JSON
        with open("data.json", "w") as f:
            json.dump(games, f, indent=4)

        # Show success message on the same page
        return render_template("add_game.html", message="Game added successfully!")

    # GET request just shows the form
    return render_template("add_game.html")

# ---------------------------- SHOW GAME LIST ------------------------------- #
# Show List Games Page
@app.route("/list")
def list_games():
    # Read existing data safely
    try:
        with open("data.json", "r") as f:
            content = f.read().strip()
            if content:
                games = json.loads(content)
            else:
                games = []
    except FileNotFoundError:
        games = []

    # Pass the games list to the template
    return render_template("list_games.html", games=games)

# ---------------------------- FILTER GAMES ------------------------------- #
# Show Filter Games Page
@app.route("/filter", methods=["GET", "POST"])
def filter_games():
    filtered_games = []
    selected_num_players = None
    selected_categories = []

    if request.method == "POST":
        # Get form data
        selected_num_players = int(request.form.get("numplayers"))
        selected_categories = request.form.getlist("category")  # list of selected categories

        # Read games from JSON
        try:
            with open("data.json", "r") as f:
                content = f.read().strip()
                if content:
                    games = json.loads(content)
                else:
                    games = []
        except FileNotFoundError:
            games = []

        # Define mutually exclusive pairs
        exclusive_pairs = [
            ("simple", "complicated"),
            ("quick", "long"),
            ("couch", "table")
        ]

        # Determine categories to exclude
        exclude_categories = set()
        for cat1, cat2 in exclusive_pairs:
            if cat1 in selected_categories:
                exclude_categories.add(cat2)
            elif cat2 in selected_categories:
                exclude_categories.add(cat1)

        # Filter games
        for game in games:
            if game["min_players"] <= selected_num_players <= game["max_players"]:
                if selected_categories:
                    if any(cat in game["tags"] for cat in selected_categories):
                        if not any(cat in game["tags"] for cat in exclude_categories):
                            filtered_games.append(game)
                else:
                    filtered_games.append(game)

    return render_template(
        "filter_games.html",
        filtered_games=filtered_games,
        selected_num_players=selected_num_players,
        selected_categories=selected_categories
    )



# ---------------------------- PICK A RANDOM GAME ------------------------------- #
# Show Pick Random Game Page
@app.route("/random")
def random_game():
    return render_template("random_game.html")

# ---------------------------------------------------------- #
if __name__ == "__main__":
    app.run(debug=True)
