# This is the main file of the chatbot though we need not run it because it has been merged with app.py file

from chat import get_response
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.get("/")
def index_get():
    # return render_template("base.html") # originally a base.html but merged with zomato rating prediction
    return render_template("Zomato.html")


# for conversation with the chatbot
# the response is received by it and then gives reply according to what model has taught it.
@app.post("/pred")
def pred():
    text = request.get_json().get("message")
    # we now see if the message is valid one or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run()
