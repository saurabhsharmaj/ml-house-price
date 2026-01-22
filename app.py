from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("house_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    price = model.predict([[data['size'], data['bedrooms'], data['age']]])
    return jsonify({"predicted_price": int(price[0])})

app.run(debug=True)
