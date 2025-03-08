import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

def train_random_forest(X_train, y_train):
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    joblib.dump(model, path)

if __name__ == "__main__":
    data = pd.read_csv("data/mosquito_habitat_dataset.csv")
    X = data.drop(columns=['Habitable','Area Name'])
    y = data['Habitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    rf_model = train_random_forest(X_train, y_train)
    save_model(rf_model, "src/models/random_forest.pkl")
    print("Random Forest model saved successfully!")
