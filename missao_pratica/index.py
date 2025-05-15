import pandas as pd
file_path = '../data_corrected.csv'
data_frame = pd.read_csv(file_path, sep = ",", engine = "python" )


# print(f"5.1: Imprima as informações gerais sobre o conjunto de dados:\n")
# data_frame.info()
# print("\n==========================================================\n")
# print(f"5.2: Imprima as primeiras N linhas do arquivo:\n")
# print(data_frame.head())
# print("\nE essas são as últimas N linhas:\n")
# print(data_frame.tail())
# print(data_frame['Date'])

# print('Corrigindo as calorias: ')
new_data_frame = data_frame.copy()
new_data_frame['Calories'] = new_data_frame['Calories'].fillna(0)
# print(f'valor das calorias atualizado: \n {new_data_frame["Calories"]}')
print('Corrigindo as Datas: ')
def normalize_date(value): 
  if pd.isna(value): return '1900/01/01'

  if isinstance(value, int) or (isinstance(value, str) and value.isdigit() and len(value) == 8):
    return f'{str(value)[:4]}/{str(value)[4:6]}/{str(value)[6:]}'
  
  if isinstance(value, str) and '/' in value: return value.strip("'")

  return '1900/01/01'

new_data_frame['Date'] = new_data_frame['Date'].apply(normalize_date)
new_data_frame['Date'] = pd.to_datetime(new_data_frame['Date'], format='%Y/%m/%d', errors= 'coerce' )
# print(new_data_frame['Date'] )

new_data_frame = new_data_frame[new_data_frame['Date'] != pd.Timestamp('1900-01-01')]
new_data_frame.reset_index(drop=True, inplace=True)
# print(new_data_frame['Date'] )

print(new_data_frame)
