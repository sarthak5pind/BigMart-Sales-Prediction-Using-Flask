import os
import pickle
import numpy as np
import pandas as pd
from flask import Flask, request, json, render_template,jsonify

app = Flask(__name__)

model = pickle.load(open('Big Mart/BigMart_model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template("home.html")


@app.route('/predict', methods=['POST', 'GET'])
def result():

    item_weight = float(request.form['item_weight'])
    item_fat_content = float(request.form['item_fat_content'])
    item_visibility = float(request.form['item_visibility'])
    item_type = float(request.form['item_type'])
    item_mrp = float(request.form['item_mrp'])
    outlet_establishment_year = float(request.form['outlet_establishment_year'])
    outlet_size = float(request.form['outlet_size'])
    outlet_location_type = float(request.form['outlet_location_type'])
    outlet_type = float(request.form['outlet_type'])

    X = np.array([[item_weight, item_fat_content, item_visibility, item_type, item_mrp,
                 outlet_establishment_year, outlet_size, outlet_location_type, outlet_type]])

    X.reshape(1,-1)
    

    prediction = model.predict(X)

    return render_template('home.html', prediction_text = f'Predicted Sale is: {prediction}')


if __name__ == "__main__":
    app.run(debug=True)