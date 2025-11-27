import pandas as pd

# Load dataset
df = pd.read_csv('../data/sample_sales.csv')

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values
df = df.fillna({'Sales': 0, 'Profit': 0})

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Save cleaned data
df.to_csv('../data/sales_cleaned.csv', index=False)
print("Data cleaning complete. Cleaned data saved to sales_cleaned.csv")
