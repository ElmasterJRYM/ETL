# importamos las librerias pandas y re.
import pandas as pd
import re

# Cargamos el archivo Excel.
nombre_archivo = 'datos.xlsx'
df = pd.read_excel(nombre_archivo)

# Función para procesar los datos de 'origin' y 'location del '
#los parametros son row(fila actual del DF) y column name(nombre de la columa a procesar) 
def procesar_datos(row, column_name):
    if row[column_name] == "{'name': 'unknown', 'url': ''}": #si el valor en la columna es igual a "{'name': 'unknown', 'url': ''},devuelve la cadena 'unknown'.
        return 'unknown'
    else:
        data_dict = eval(row[column_name]) #Si no,utiliza la función eval() para convertir el valor de la columna en un diccionario.
        name = data_dict['name'] #extrae el nombre y el identificador de ubicación del diccionario y los combina en una cadena de texto que se devuelve.
        url_parts = data_dict['url'].split('/')
        location = url_parts[-1]
        return f"{name}, location {location}"
    
#funcion para procesar los datos de 'image'    
def procesar_imagen(row): #tomamos una fila del dataframe como argumento
    url_parts = row['image'].split('/') #Dividimos la URL utilizando la barra diagonal como separador y toma la última parte.
    identifier = url_parts[-1].split('.')[0] #dividimos el nombre de archivo para quitar la extensión del archivo.
    return f"avatar {identifier}" #combinamos el identificador resultante con la palabra avatar

# funcion para procesar los datos de 'episode'
def procesar_episodio(row): #tomamos la ultima fila del dataframe como argumento
    episodes = row['episode'] #obtenemos el contenido de la columna episode
    episode_numbers = re.findall(r'\d+', episodes) #ocupamos la expresion regular (re.findall()) para encontrar todos los números en la lista de URLs.
    return ', '.join(episode_numbers) #unimos los numeros obtenidos separados por comas

# Aplicar las funciones a las columnas correspondientes
df['origin'] = df.apply(lambda row: procesar_datos(row, 'origin'), axis=1)
df['location'] = df.apply(lambda row: procesar_datos(row, 'location'), axis=1)
df['image'] = df.apply(procesar_imagen, axis=1)
df['episode']= df.apply(procesar_episodio, axis=1)

# Guardar el DataFrame actualizado en un nuevo archivo Excel
nombre_archivo_actualizado = 'datos_actualizados.xlsx'
df.to_excel(nombre_archivo_actualizado, index=False)