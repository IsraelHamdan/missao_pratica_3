import pandas as pd

file_path = '../data_corrected.csv'
df = pd.read_csv(file_path)

print(df.head(32))
print(df.info())

# Exibir estatísticas básicas
print(df.describe())