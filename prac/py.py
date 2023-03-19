import pandas as pd
melb_data = pd.read_csv('E:\SF\date\melb_data.csv', sep=',')
print(melb_data.iloc[3521])
print(melb_data.iloc[1690])
s = round(melb_data.loc[3521,'Landsize']) / (melb_data.loc[1690,'Landsize'])
print(s)