import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

file_path = "../datasets/processed.csv"
file_path = "../datasets/air_df_correct_format.csv"
data = pd.read_csv(file_path, delimiter=';')

# display(data.head(10))

data.columns = [col.strip() for col in data.columns]

# check for required columns
if 'Date' in data.columns and 'Time' in data.columns:
    data['DateTime'] = pd.to_datetime(data['Date'] + ' ' + data['Time'], format='%d/%m/%Y %H.%M.%S')
else:
    raise ValueError("Required columns 'Date' and 'Time' not found in the dataset.")

# select numeric columns for visualization
numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns

# --- Plotly: interactive graphs ---
for col in numeric_cols:
    fig = px.line(data, x='DateTime', y=col, title=f'Interactive Time Series for {col}')
    fig.update_layout(xaxis_title='DateTime', yaxis_title=col, template='plotly_dark')
    fig.show()
