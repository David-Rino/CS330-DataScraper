import pandas as pd

df = pd.read_excel("data.xlsx")

print(df.head())

class PandasModel:
    def __init__(self, file_path):
        try:
            self.df = pd.read_excel(file_path)
        except Exception as e:
            print(f"Error reading the Excel file: {e}")

