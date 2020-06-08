from flask import Flask, request, jsonify
import util
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price1', methods=['GET', 'POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_sqft,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_home_price2', methods=['GET', 'POST'])
def predict_home_price2():
    bedrooms=float(request.form['bedrooms'])
    bathrooms=float(request.form['bathrooms'])
    sqft_lv=float(request.form['sqft_lv'])
    sqft_lot=float(request.form['sqft_lot'])
    floors=float(request.form['floors'])
    condition=float(request.form['condition'])
    grade=float(request.form['grade'])
    sqft_above=float(request.form['sqft_above'])
    sqft_basement=float(request.form['sqft_basement'])
    lat=float(request.form['lat'])
    longg=float(request.form['longg'])

    response = jsonify({
        'estimated_price': util.get_estimated_price2(bedrooms,bathrooms,sqft_lv,sqft_lot,floors,condition,grade,sqft_above,sqft_basement,lat,longg)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()