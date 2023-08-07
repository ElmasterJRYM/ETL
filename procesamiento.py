#importaremos la libreria json y la libreria pandas.
import json
import pandas as pd

# Cargar el archivo JSON que obtuvimos con el programa "obtener datos.py"
with open('datos_api.json', 'r') as json_file:
    data = json.load(json_file)

# utilizamos pandas para crear un dataframe.
df = pd.DataFrame(data['results'])

# definimos el nombre del archivo Excel.
nombre_archivo = 'datos.xlsx'

# Guardamos el dataframe generado en el archivo excel.
df.to_excel(nombre_archivo, index=False)
