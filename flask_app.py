# library that allows us to load machine learning models and deploy them via flask
import pickle

from flask import Flask, request
import pandas as pd


# libraries for UI
# import flasgger

# swagger will generate UI
from flasgger import Swagger


app = Flask(__name__)
# tells flask to generate UI
Swagger(app)

# open classifier in read-byte mode
# open("/Users/johnowusuduah/github/docker_ml_project/classifier.pkl", "rb")
pickle_in = open("classifier.pkl", "rb")
# load the opened classifier file
classifier = pickle.load(pickle_in)

# we define route path of url/port....500 (what should display when you land on page)
@app.route("/")
def welcome():
    """Function that welcomes clients to the webpage"""
    return "Welcome. This application runs predictions on whether a bank note is genuine or fake"


# define a function that takes four features in our ml model and makes a prediction via our GET API
# http://127.0.0.1:5000/predict?variance=2&skewness=3&curtosis=2&entropy=1
# this is also a get method
@app.route("/predict", methods=["Get"])
def predict_note_authentication():

    """This API runs predictions on whether a bank note is genuine or fake given its features.

    Kindly click "Execute" after entering parameters.
    ---
    parameters:
        - name: variance
          in: query
          type: number
          required: true
        - name: skewness
          in: query
          type: number
          required: true
        - name: curtosis
          in: query
          type: number
          required: true
        - name: entropy
          in: query
          type: number
          required: true
    responses:
        200:
            description: The output values
    """
    variance = request.args.get("variance")
    skewness = request.args.get("skewness")
    curtosis = request.args.get("curtosis")
    entropy = request.args.get("entropy")
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    if prediction[0] == 0:
        return "The value of the note is 0. Thus, the model predicts that the bank not is fake."
    else:
        return "The value of the note is 1. Thus, the model predicts that the bank not is genuine."


# we would like to define a function that allows batch predictions to be made from test csv files
# which we will be inserting
# post method allows us to insert/update remote data.
@app.route("/predict_file", methods=["POST"])
def predict_note_file():

    """Let us Authenticate Bank Notes
    This uses docstrings for specifications
    ---
    parameters:
        - name: file
          in: formData
          type: file
          required: true

    responses:
        200:
            description: The output values

    """
    df_test = pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction = classifier.predict(df_test)

    return "The predicted values for the csv is " + str(list(prediction))


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
