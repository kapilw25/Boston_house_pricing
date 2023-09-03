import pickle   
from Flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# load the model from disk
regmodel=pickle.load(open('regmodel.pkl','rb')) #rb = read binary mode
scalar=pickle.load(open('scaling.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST']) #post = send data to server via POSTMAN 

def predict_api():
    data=request.json['data']
    print(data)

