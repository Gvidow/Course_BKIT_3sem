from flask import Flask
from catalan_numbers import catalan_numbers_gen


app = Flask(__name__)


@app.route("/")
def main_page():
    return "<h3>Catalan number sequence generator</h3>"


@app.route("/catalan/<int:num>")
def get_catalan_numbers(num):
    catalan = catalan_numbers_gen()
    return [next(catalan) for _ in range(num)]


if __name__ == "__main__":
    app.run(host="localhost", port=8080)
