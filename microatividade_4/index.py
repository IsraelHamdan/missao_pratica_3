import pandas as pd
file_path = '../data_corrected.csv'
data_frame = pd.read_csv(file_path, sep = ",", engine = "python" )

print(data_frame.head(10))