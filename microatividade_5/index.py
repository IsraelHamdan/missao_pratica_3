import pandas as pd
file_path = '../data_corrected.csv'
data_frame = pd.read_csv(file_path, sep = ",", engine = "python" )

total_rows = len(data_frame)
print(f'esta é a quantidade de linhas: {total_rows}')

total_columns = len(data_frame.columns)
print(f'\n esta é a quantidade de columns: {total_rows}')

null_values = data_frame.isnull().sum().sum()
print(f'\n esta é a quantidade de informações nulas: {null_values}')

data_types = data_frame.dtypes 
print(f'estes são os tipos de dados encontrados: {data_types}')

memory_usage = data_frame.memory_usage(deep=True).sum()
print(f'A quantidade de memória usada é: {memory_usage}')