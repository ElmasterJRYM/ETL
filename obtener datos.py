#importamos las librerias requests y json.
import requests
import json
#definimos la url de la api que vamos a utilizar
api_url = "https://rickandmortyapi.com/api/character"
# Realizo la solicitud GET a la API de Rick and Morty para obtener información.
response = requests.get(api_url)
# utilizo una verificacion de que la solicitud se realizo con exito.
if response.status_code == 200:
    # Convierte los datos de la respuesta en formato JSON.
    json_data = response.json()
    # Guarda los archivos en 'datos_api.json' con formato indentado.
    with open('datos_api.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)
    # Imprime un mensaje de éxito.
    print("Datos guardados en datos_api.json")
else:
    # Imprime un mensaje de error.
    print("Error al obtener datos de la API. Código de estado:", response.status_code)
