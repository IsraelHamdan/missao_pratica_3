import pandas as pd

file_path = '../data_corrected.csv'


data_frame = pd.read_csv(file_path, sep = ",", engine = "python")
subset_data = data_frame[["ID", "Date", "Calories"]]

print(subset_data)