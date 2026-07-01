from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from database import products
import os

app = Flask(__name__)

# -----------------------------
# Configuration
# -----------------------------
UPLOAD_FOLDER = "static/uploads"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -----------------------------
# Home Page
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Show All Products
# -----------------------------
@app.route("/products")
def show_products():

    all_products = list(products.find())

    return render_template(
        "products.html",
        products=all_products
    )


# -----------------------------
# Search Products
# -----------------------------
@app.route("/search", methods=["POST"])
def search():

    query = request.form.get("query")

    if not query:
        return render_template(
            "search.html",
            products=[],
            query=""
        )

    result = list(products.find({
        "$or": [

            {
                "name": {
                    "$regex": query,
                    "$options": "i"
                }
            },

            {
                "brand": {
                    "$regex": query,
                    "$options": "i"
                }
            },

            {
                "category": {
                    "$regex": query,
                    "$options": "i"
                }
            }

        ]
    }))

    return render_template(
        "search.html",
        products=result,
        query=query
    )


# -----------------------------
# Upload Image
# -----------------------------
@app.route("/upload", methods=["POST"])
def upload():

    if "image" not in request.files:

        return "No Image Selected"

    image = request.files["image"]

    if image.filename == "":

        return "Choose Image"

    filename = secure_filename(image.filename)

    filepath = os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )

    image.save(filepath)

    return render_template(
        "result.html",
        image=filename
    )


# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":

    app.run(
        debug=True
    )