from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("../web/random_forest.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json  

    # Convert categorical inputs to numerical values
    mapping = {
        "Low": {"daily_avg_temp": 22.53, "total_precipitation": 25.08, "relative_humidity": 52.70, "population_density": 2565.32, "day_length": 11.00},
        "Medium": {"daily_avg_temp": 27.41, "total_precipitation": 50.14, "relative_humidity": 65.38, "population_density": 5030.63, "day_length": 11.99},
        "High": {"daily_avg_temp": 32.31, "total_precipitation": 75.06, "relative_humidity": 77.69, "population_density": 7514.82, "day_length": 12.99},
        "Yes": 1,
        "No": 0,
        "Urban": 1,
        "Rural": 0
    }

    input_features = np.array([
        22.53,  # Fixed daily_min_temp
        32.31,  # Fixed daily_max_temp
        mapping[data["daily_avg_temp"]]["daily_avg_temp"],
        mapping[data["total_precipitation"]]["total_precipitation"],
        mapping[data["relative_humidity"]]["relative_humidity"],
        mapping[data["water_bodies"]],
        mapping[data["population_density"]]["population_density"],
        mapping[data["day_length"]]["day_length"],
        mapping[data["urban_rural_area"]],
        mapping[data["forested_area"]],
        mapping[data["crop_area"]],
        mapping[data["graze_land_area"]]
    ]).reshape(1, -1)

    prediction = model.predict(input_features)[0]

    return jsonify({"prediction": int(prediction)})

if __name__ == "__main__":
    app.run(debug=True)
