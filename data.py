import pandas as pd

# Load the dataset
data = pd.read_csv('data/mosquito_habitat_dataset.csv')

# Select only continuous variables (those that are numerical)
continuous_columns = [ 'Daily Avg Temp', 
    'Total Precipitation', 'Relative Humidity',
    'Population Density', 'Day Length'
]

# Create a dictionary to store results
results = {}

# Calculate the min, max, and mean for each continuous column
for col in continuous_columns:
    col_min = data[col].min()
    col_max = data[col].max()
    col_mean = data[col].mean()
    
    # Calculate Low, Medium, High values
    low_value = (col_min + col_mean) / 2
    medium_value = col_mean
    high_value = (col_mean + col_max) / 2
    
    # Store the results
    results[col] = {
        'Low': low_value,
        'Medium': medium_value,
        'High': high_value
    }

# Output the results
for col, values in results.items():
    print(f"Column: {col}")
    print(f"Low: {values['Low']}")
    print(f"Medium: {values['Medium']}")
    print(f"High: {values['High']}")
    print()
