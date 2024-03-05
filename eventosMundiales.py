import pandas as pd
from pprint import pprint
from termcolor import colored

class CFG:
    class path:
        to_data = "Olimpiadas.csv"
    class data:
        columns = ['Gender', 'Event', 'Location', 'Year', 'Medal', 'Name', 'Nationality', 'Result']

df = pd.read_csv(CFG.path.to_data, names=CFG.data.columns, index_col=1)
df = df.sort_values(by="Year").reset_index()
df = df[df.Gender != "Gender"]
df['Event'] = df['Event'].str.replace(' Men', '').str.replace(' Women', '')

df.to_csv('OlimpiadasResultados.csv',encoding="utf-8")
