import pandas as pd
import numpy as np

# Set the random seed for reproducibility
np.random.seed(42)

# Number of samples
num_samples = 1000

# Generate synthetic data
data = {
    'Temperature': np.random.uniform(15, 35, num_samples),  # Temperature in degrees Celsius
    'Humidity': np.random.uniform(20, 80, num_samples),     # Humidity in percentage
    'R_450': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 450 nm
    'R_550': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 550 nm
    'R_650': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 650 nm
    'R_720': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 720 nm
    'R_750': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 750 nm
    'R_800': np.random.uniform(0.1, 0.9, num_samples),      # Reflectance at 800 nm
    'Efficiency': np.random.uniform(10, 25, num_samples)    # Solar panel efficiency in percentage
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv('Data_BarbeauFlux_noNaN.csv', sep=';', decimal='.', index=False)
