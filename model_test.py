from flask import Flask, request
import numpy as np 
import pandas as pd
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

#Loading model using pickle file 
pickle_file_open = open("bank_note_verification.pkl","rb")
classifier = pickle.load(pickle_file_open)

@app.route('/',methods=['GET'])
def welcome_message():
    try:
        return "Welcome to praxis",200
    except Exception as e:
        return "something went wrong",400

@app.route('/predict',methods=['GET'])
def predict():
   
    """Testing of prediction .
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
            description: The response is 
        
    """

    var = request.args.get("variance")
    skew = request.args.get("skewness")
    curt = request.args.get("curtosis")
    ent = request.args.get("entropy")
    result = classifier.predict([[var,skew,curt,ent]])
    if result in [0,"0"] :  return "Fake Bank Note",200
    return "Valid bank note",200

@app.route('/predict_through_file',methods=["POST"])
def predict_file():
    """Testing of prediction using Test file
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The response of file is         
    """

    df = pd.read_csv(request.files.get("file"))
    print("-"*30+" File details "+"-"*30)
    print(df.shape)
    print(df.head())
    print("-"*70)
    result = classifier.predict(df)
    return f"The result are as follows {result}"


if __name__ == "__main__":
    app.run(debug=True)