import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

URL = "https://es.wikipedia.org/wiki/Anexo:Tabla_estad%C3%ADstica_de_la_Copa_Mundial_de_F%C3%BAtbol"

page = requests.get(URL) # Se realiza la peticion a la página en este caso a una pagina de WikiPedia

soup = bs(page.content, features="html.parser") # Se obtiene el contenido de la pagina en etiquetas, gracias a la libreria de BeautifulSoup

table = soup.select('table')[0] #Seleccionamos la tabla a analizar, en este caso será la primera

table_df = pd.read_html(str(table),index_col=0)[0] #Utilizando la libreria de panda, nos permite transformar html a un dataframe

table_df = table_df.drop(['Títulos'],axis=1) #Eliminamos la columna de titulos debido a que tiene muchos valores vacíos

table_df = table_df[:50] # Solo trabajaremos con los 50 primeros registros
print(table_df)
table_df.to_csv('EstadisticasFasesFinales.csv',encoding='utf-8')