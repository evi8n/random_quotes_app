from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def index():
    # Fetch a random quote from the Quotable REST API
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
    else:
        quote = "Error fetching quote"
        author = "Unknown"

    # Render the template with the quote and author
    return render_template("index.html", quote=quote, author=author)


@app.route("/new_quote")
def new_quote():
    # Fetch a new random quote from the Quotable REST API
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data["content"]
        author = quote_data["author"]
    else:
        quote = "Error fetching quote"
        author = "Unknown"

    # Return the new quote as JSON
    return jsonify({"quote": quote, "author": author})


if __name__ == "__main__":
    app.run(debug=True)