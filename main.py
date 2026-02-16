from flask import Flask


app = Flask(__name__)

count = [0]


@app.route("/")
def index():
    count[0] += 1
    return "Hello from Barcelona 2026."


if __name__ == "__main__":
    app.run(debug=True)
