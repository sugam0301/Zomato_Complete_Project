from flask import Flask, render_template, request, jsonify
from chat import get_response

app = Flask(__name__)


@app.get("/")
def index_get():

    return render_template("Zomato.html")


@app.post("/pred")
def pred():
    text = request.get_json().get("message")
    # we now see if the message is valid one or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run()
