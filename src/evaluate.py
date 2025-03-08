import joblib
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split

def load_data():
    return pd.read_csv("data/mosquito_habitat_dataset.csv")

def evaluate_model(model, X_test, y_test):
    preds = model.predict(X_test)
    return {
        "Accuracy": accuracy_score(y_test, preds),
        "Precision": precision_score(y_test, preds),
        "Recall": recall_score(y_test, preds),
        "F1-Score": f1_score(y_test, preds),
        "ROC AUC": roc_auc_score(y_test, preds)
    }

if __name__ == "__main__":
    data = load_data()
    X = data.drop(columns=['Habitable','Area Name'])
    y = data['Habitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    models = {
        "Random Forest": joblib.load("src/models/random_forest.pkl"),
        "XGBoost": joblib.load("src/models/xgboost.pkl"),
        "Genetic Algorithm": joblib.load("src/models/genetic_algorithm.pkl")
    }

    for name, model in models.items():
        metrics = evaluate_model(model, X_test, y_test)
        print(f"{name} Performance: {metrics}")
