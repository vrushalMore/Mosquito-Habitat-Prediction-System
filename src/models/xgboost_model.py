import joblib
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split

def train_xgboost(X_train, y_train):
    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    joblib.dump(model, path)

if __name__ == "__main__":
    data = pd.read_csv("data/mosquito_habitat_dataset.csv")
    X = data.drop(columns=['Habitable','Area Name'])
    y = data['Habitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    xgb_model = train_xgboost(X_train, y_train)
    save_model(xgb_model, "src/models/xgboost.pkl")
