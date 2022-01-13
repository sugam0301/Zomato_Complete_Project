#main file where we run our app and FLASK API

import numpy as np
from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
import os
from chat import get_response

from flask_cors import CORS, cross_origin

'''Load pickle file'''
# file = os.listdir('./bestmodel/')[3]
# print("file")
with open('model_pickle', 'rb') as file:
    model = pickle.load(file)
# with open('model_pickle','rb') as file:
#     scaler = pickle.load(file)
# scaler = pickle.load(open('std_scaler.pkl','rb'))

app = Flask(__name__)


@app.route('/')
@cross_origin()
def home():
    return render_template('Zomato.html')


#In this the main prediction plus the html part of the chatbot is linked
@app.route('/predict', methods=['POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        city = int(request.form['City'])
        location = int(request.form['Location'])
        cuisine = int(request.form['Cuisine'])
        no_of_reviews = int(request.form['No. of Reviews'])
        price = int(request.form['Price'])

        final_features = [np.array((city, location, cuisine, no_of_reviews, price))]

        prediction = model.predict(final_features)
        output = round(prediction[0], 2)

        return render_template('result.html', output=f"Predicted Rating is: {str(output)}")
    else:
        return render_template('Zomato.html')


# This is used for functioning of Chatbot
@app.post("/pred")
@cross_origin()
def pred():
    text = request.get_json().get("message")
    # we now see if the message is valid one or not
    response = get_response(text)
    message = {"answer": response}
    return jsonify(message)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
