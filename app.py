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
    return render_template('home.html') #render the html page

@app.route('/predict_api',methods=['POST']) #post = send data to server via POSTMAN 

def predict_api():
    data=request.json['data']
    print(data) # data is in key value pair
    print(np.array(list(data.values())).reshape(1,-1))  #convert data into array
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1)) #transform data into scalar
    output = regmodel.predict(new_data) #predict the data
    print(output[0])
    return jsonify(output[0]) #return the output in json format 

if __name__ == "__main__":
    app.run(debug=True) # run the app in debug mode, so that we can see the error in browser
    
    
    
     
    

