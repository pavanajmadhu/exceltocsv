import pandas as pd

read_file = pd.read_excel (r"mark.xlsx")
read_file.to_csv (r'test.csv', index = None, header=True)
