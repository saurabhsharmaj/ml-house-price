from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load("house_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    price = model.predict([[data['size'], data['bedrooms'], data['age']]])
    return jsonify({"predicted_price": int(price[0])})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

