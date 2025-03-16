import pandas as pd

# Load the Excel file
file_path = "/mnt/data/Building a sales forecasting model dataset.xlsx"

# Load all sheet names
xls = pd.ExcelFile(file_path)
xls.sheet_names
# Load the data from the first sheet
df = pd.read_excel(file_path, sheet_name='Sheet1')

# Display the first few rows of the dataset
import ace_tools as tools
tools.display_dataframe_to_user(name="Sales Forecasting Dataset", dataframe=df)