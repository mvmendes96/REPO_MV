import pandas as pd



df = pd.read_excel('escalas.xlsx')


print(df,"")



# pd.read_excel(open('tmp.xlsx', 'rb'),sheet_name='Sheet3')

teste = pd.read_excel('escalas.xlsx', sheet_name='escolta')

print(teste)