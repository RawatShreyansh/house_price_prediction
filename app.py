import pickle
from flask import Flask,request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd

app = Flask(__name__)

regmodel = pickle.load(open('./model/regmodel.pkl','rb'))
scaler = pickle.load(open('./model/scaler.pkl','rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    data = np.array(list(data.values())).reshape(1,-1)
    new_data = scaler.transform(data)
    output = regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data = request.form.to_dict()
    print(data)
    data = np.array(list(data.values())).reshape(1,-1)
    new_data = scaler.transform(data)
    output = regmodel.predict(new_data)
    print(output[0])
    return render_template('home.html',prediction_text='The predicted value is {}'.format(output[0]))

if __name__ == "__main__":
    app.run(debug=True)