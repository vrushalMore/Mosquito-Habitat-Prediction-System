# Mosquito Habitat Prediction System

## Problem Statement
Mosquito-borne diseases are a major public health concern. This system predicts whether a location is habitable for mosquitoes based on environmental parameters. The goal is to help authorities and researchers take preventive actions against mosquito infestations.

## Solution
This project implements a machine learning-based prediction system using a **Random Forest model** trained on relevant environmental features. A **web-based interface** allows users to input parameters, and the backend processes these inputs to return a prediction.

## Pipeline
The project follows a structured pipeline to ensure efficient data processing and accurate predictions:

1. **Data Collection**: The dataset (`mosquito_habitat_dataset.csv`) contains environmental parameters that influence mosquito habitat suitability.
2. **Preprocessing**:
   - Missing value handling, feature encoding, and scaling are performed (`preprocessing.py`).
   - The cleaned data is stored as `preprocessed_data.csv`.
3. **Model Training**:
   - Three models are trained: Random Forest, XGBoost, and Genetic Algorithm (`random_forest.py`, `xgboost_model.py`, `genetic_algorithm.py`).
   - The trained models are stored as `.pkl` files in `src/models/`.
4. **Model Evaluation**:
   - The models are evaluated based on metrics like accuracy, precision, recall, and F1-score (`evaluate.py`).
   - Random Forest is selected as the best model for deployment.
5. **Web Application**:
   - A user-friendly frontend (`index.html`) with sliders and dropdowns for parameter input.
   - A FastAPI backend (`app.py`) loads the Random Forest model and provides predictions.
6. **Deployment**:
   - The application runs locally, and predictions are served via API endpoints.

## Project Directory Structure
```
mosquito_habitat_prediction/
│── data/
│   ├── mosquito_habitat_dataset.csv
│   ├── preprocessed_data.csv
│── src/
│   ├── data_analysis.ipynb
│   ├── evaluate.py
│   ├── preprocessing.py
│   ├── models/
│   │   ├── genetic_algorithm.pkl
│   │   ├── genetic_algorithm.py
│   │   ├── random_forest.pkl
│   │   ├── random_forest.py
│   │   ├── xgboost.pkl
│   │   ├── xgboost_model.py
│── web/
│   ├── app.py
│   ├── random_forest.pkl
│   ├── templates/
│   │   ├── index.html
```

## How to Run the Project
### Prerequisites
- Python 3.8+
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### Running the Web Application
```bash
cd web
python app.py
```
The application will be available at `http://127.0.0.1:8000`.

