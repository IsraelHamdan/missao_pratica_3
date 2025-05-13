import pandas as pd
file_path = '../data_corrected.csv'
data_frame = pd.read_csv(file_path, sep = ",", engine = "python" )
subset_data = data_frame[["ID", "Date", "Calories"]]
pd.set_option('display.max_rows', 9999)

print(subset_data.to_string())