import requests
import json
from bs4 import BeautifulSoup as bs
import re

URL = "https://beachvolleytour.es/10-deportes-mas-practicados-en-el-mundo/"

page = requests.get(URL)
soup = bs(page.content, features="html.parser")

titulos = soup.select('strong')[3:]
patron = r'\d+\.-\s(\w+(?:\s\w+)*)\s\(([\d\.]+ millones de practicantes)\)'  

# Lista para almacenar los datos
datos = []

for tituloHtml in titulos:
    texto = tituloHtml.get_text()
    match = re.match(patron, texto)
    if match:
        titulo = match.group(1)
        numero_practicantes = match.group(2)
        datos.append({
            "Título": titulo,
            "Número de practicantes": numero_practicantes
        })


with open("datos_deportes.json", "w", encoding="utf-8") as f:
    json.dump(datos, f, indent=4)