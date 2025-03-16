import pandas as pd

# Load the Excel file
file_path = "/mnt/data/Building a sales forecasting model dataset.xlsx"
xls = pd.ExcelFile(file_path)

# Display sheet names to understand the structure of the file
xls.sheet_names
# Load the data from the first sheet
df = pd.read_excel(xls, sheet_name='Sheet1')

# Display the first few rows to understand the structure
df.head()
# Cleaning the dataset

# 1. Convert 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# 2. Check for and handle missing values
missing_values = df.isnull().sum()

# 3. Remove duplicates if any
df = df.drop_duplicates()

# 4. Check for any anomalies (e.g., negative values in sales-related columns)
numeric_columns = ['quantity', 'unit_price', 'base_price', 'total_sales', 'sales_seasonality']
anomalies = df[df[numeric_columns] < 0].any()

# Display cleaned dataset and missing values report
import ace_tools as tools

tools.display_dataframe_to_user(name="Cleaned Sales Data", dataframe=df)

# Display missing values report
missing_values, anomalies
# Estimating missing dates

# Approach: Use forward-fill method where possible; otherwise, use the median date
df['date'] = df['date'].fillna(method='ffill')  # Forward fill first

# If any missing values remain, fill them with the median date of the dataset
median_date = df['date'].median()
df['date'] = df['date'].fillna(median_date)

# Verify that all missing dates are filled
missing_dates_after = df['date'].isnull().sum()

# Display the updated dataset
tools.display_dataframe_to_user(name="Updated Sales Data with Estimated Dates", dataframe=df)

missing_dates_after