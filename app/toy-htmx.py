from flask import Flask, render_template

app = Flask(__name__)


@app.get("/ingredients")
def ingredients():
    return render_template("partials/ingredients.html")


@app.get("/ingredient-list")
def get_ingredients():
    ingredients = [
        "1 small onion",
        "2 tomatoes",
        "1 garlic clove",
        "1 bay leaf",
        "1 tablespoon",
        "12 oz lager beer",
        "3 tablespoons butter",
        "1 cup beef broth",
        "3/4 cup port wine",
        "1 tablespoon",
        "salt and pepper",
    ]

    return render_template("partials/ingredient-list.html", ingredients=ingredients)


# Navbar could be in the static HTML, this is a behavior test of trigger-less
# AJAX content.
@app.get("/navbar")
def get_navbar():
    return render_template("partials/navbar.html")


@app.get("/document")
def get_document():
    return render_template("partials/document.html")


@app.route("/")
def hello_world():
    return render_template("index.html")
