from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Her kan man regne vektor ud i 2D<h1> <h2>Din vektor<h2>"

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"



if __name__ == "__main__":
    app.run()
