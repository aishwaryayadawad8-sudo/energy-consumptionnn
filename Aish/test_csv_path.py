import os
import sys

# Add the sustainable_energy directory to the path
sys.path.insert(0, 'sustainable_energy')

# Simulate the path calculation from views.py
file_path = 'sustainable_energy/dashboard/views.py'
csv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(file_path))), 'global-data-on-sustainable-energy.csv')

print(f"Calculated CSV path: {csv_path}")
print(f"File exists: {os.path.exists(csv_path)}")
print(f"Absolute path: {os.path.abspath(csv_path)}")

# Try to read it
import pandas as pd
try:
    df = pd.read_csv(csv_path)
    print(f"Successfully loaded CSV with {len(df)} rows")
    print(f"Countries: {len(df['Entity'].unique())}")
except Exception as e:
    print(f"Error: {e}")
