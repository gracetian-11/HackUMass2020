from flask import Flask
from datastax_astra import connect

app = Flask(__name__)


@app.route("/")
def hello():
    connect()
    return "Hello World!"


if __name__ == "__main__":
    app.run(debug=True)