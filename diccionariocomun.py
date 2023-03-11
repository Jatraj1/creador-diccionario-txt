import re
import nltk
from collections import Counter
import requests
from bs4 import BeautifulSoup
import nltk
import PyPDF2
#   DICCIONARIO FORMATO .TXT DE LAS PALABRAS MÁS USADAS EN UNA WEB EN ORDEN DE CANTIDAD DE VECES USADAS
#   Soy consciente de que es muy poco eficiente y no está hecho de la manera más adecuada/correcta pero funciona y es por eso que lo quiero subir por si algun@ lo necesitais para crear un diccionario de las palabras más frecuentes en cierta web


# URL de la página web de la que deseas obtener las palabras
# url = 'https://corpus.rae.es/frec/10000_formas.TXT'

# Obtenemos el contenido HTML de la página web y extraemos el texto utilizando Beautiful Soup
# html = requests.get(url).content
# soup = BeautifulSoup(html, 'html.parser')
# texto = soup.get_text()


# Sacar las palabras de un txt

with open("setienequemorirmuchagente.txt", encoding="utf-8") as archivo:
    texto = archivo.read()


# Creamos una expresión regular que solo permite letras, espacios y signos de puntuación necesarios
texto = texto.lower()
regex = re.compile('[^\wáéíóúÁÉÍÓÚñÑ ]')


# Eliminamos los caracteres no deseados (comas, puntos, paréntesis, etc)
texto = regex.sub(' ', texto)
texto_sin_numeros = ""

# Eliminamos los números (lo hago de esta manera porque en la variable regex aunque introdujera \d no me funcionaba)
for caracter in texto:
    if not caracter.isnumeric():
        texto_sin_numeros += caracter

texto = texto_sin_numeros

# Tokenizamos para saber las palabras más comunes del texto
textos = [texto]
tokens = []
for texto in textos:
    palabras = nltk.word_tokenize(texto.lower())
    tokens += palabras

contador = Counter(tokens)

# Introduce en la variable numero_de_palabras el número de palabras que quieres que tenga el diccionario (ej: si numero_de_palabras = 3 solo se mostrarán las 3 palabras más usadas)
numero_de_palabras = 10000
palabras_comunes = contador.most_common(numero_de_palabras)

# Preparamos el formato de output para que solo salgan las palabras, una por línea (\n)
palabras_formateadas = [
    f"{palabra}: {contador}" for palabra, contador in palabras_comunes]

formatodict = "\n".join(palabras_formateadas)

lineas = formatodict.split('\n')

lineas_formateadas = [linea.split(': ')[0] for linea in lineas]

resultado = '\n'.join(lineas_formateadas)

# Imprimimos el resultado para verificar que todo está bien de forma rápida
print(resultado)

# Creamos un txt llamado dict.txt con las palabras
with open("dict.txt", mode="w", encoding="utf-8") as file:
    file.write(resultado)
