import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def load_data(file_path):
    return pd.read_csv(file_path)

def handle_missing_values(df):
    for column in df.columns:
        if df[column].dtype == 'object':
            df[column].fillna(df[column].mode()[0], inplace=True)
        else:
            df[column].fillna(df[column].mean(), inplace=True)
    return df

def encode_categorical(df):
    label_encoders = {}
    for column in df.select_dtypes(include=['object']).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
    return df, label_encoders

def scale_features(X_train, X_test):
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler

def preprocess_data(file_path, output_path):
    df = load_data(file_path)
    df = handle_missing_values(df)
    df, label_encoders = encode_categorical(df)
    
    X = df.drop(columns=['Habitable'])
    y = df['Habitable']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    
    df.to_csv(output_path, index=False)
    
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, label_encoders

if __name__ == "__main__":
    input_file = "data/mosquito_habitat_dataset.csv"
    output_file = "data/preprocessed_data.csv"
    
    X_train, X_test, y_train, y_test, scaler, encoders = preprocess_data(input_file, output_file)
