# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 19:56:02 2021

@author: Deeksha Priya
"""

from flask import Flask, request, jsonify
import util

app = Flask(__name__)  

@app.route('/get_location_names')
def get_location(): 
    response = jsonify({
       'location' :util.get_location_names()
       })
    response.headers.add('Access-control-Allow-Origin', '*')
    return response

@app.route('/predict_home_price',methods =['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath']) 

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location,total_sqft,bhk,bath)
    })

if __name__ == "__main__":
    print("Flask Server for Home Price Prediction")
    util.load_saved_artifacts()
    app.run() 