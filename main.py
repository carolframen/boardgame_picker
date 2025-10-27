# Board Game Picker
# ---------------------------- IMPORTS ------------------------------- #
from flask import Flask, render_template, request
import json
import random

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

# ---------------------------- FILTER LOGIC ------------------------------- #
def filter_games_logic(num_players, selected_categories):
    try:
        with open("data.json", "r") as f:
            content = f.read().strip()
            if content:
                games = json.loads(content)
            else:
                games = []
    except FileNotFoundError:
        games = []

    filtered_games = []

    exclusive_pairs = [
        ("simple", "complicated"),
        ("quick", "long"),
        ("couch", "table"),
    ]

    for game in games:
        if game["min_players"] <= num_players <= game["max_players"]:
            tags = game["tags"]

            # Handle mutually exclusive logic
            is_excluded = False
            for a, b in exclusive_pairs:
                if a in selected_categories and b in tags:
                    is_excluded = True
                if b in selected_categories and a in tags:
                    is_excluded = True
            if is_excluded:
                continue

            # If categories are selected, game must match at least one
            if selected_categories:
                if any(cat in tags for cat in selected_categories):
                    filtered_games.append(game)
            else:
                filtered_games.append(game)

    return filtered_games


# ---------------------------- FILTER GAMES ------------------------------- #
@app.route("/filter", methods=["GET", "POST"])
def filter_games():
    filtered_games = []
    selected_num_players = None
    selected_categories = []

    if request.method == "POST":
        selected_num_players = int(request.form.get("numplayers"))
        selected_categories = request.form.getlist("category")

        filtered_games = filter_games_logic(selected_num_players, selected_categories)

    return render_template(
        "filter_games.html",
        filtered_games=filtered_games,
        selected_num_players=selected_num_players,
        selected_categories=selected_categories
    )


# ---------------------------- PICK A RANDOM GAME ------------------------------- #
@app.route("/random", methods=["GET", "POST"])
def random_game():
    random_game = None
    selected_num_players = None
    selected_categories = []

    if request.method == "POST":
        selected_num_players = int(request.form.get("numplayers"))
        selected_categories = request.form.getlist("category")

        filtered_games = filter_games_logic(selected_num_players, selected_categories)

        if filtered_games:
            random_game = random.choice(filtered_games)

    return render_template(
        "random_game.html",
        random_game=random_game,
        selected_num_players=selected_num_players,
        selected_categories=selected_categories
    )


# ---------------------------------------------------------- #
if __name__ == "__main__":
    app.run(debug=True)
