from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("random_forest.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json 

    input_features = np.array([
        data["daily_min_temp"],
        data["daily_max_temp"],
        data["daily_avg_temp"],
        data["total_precipitation"],
        data["relative_humidity"],
        data["water_bodies"],
        data["population_density"],
        data["day_length"],
        data["urban_rural_area"],
        data["forested_area"],
        data["crop_area"],
        data["graze_land_area"]
    ]).reshape(1, -1)  

    prediction = model.predict(input_features)[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
