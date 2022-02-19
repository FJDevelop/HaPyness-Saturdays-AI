import pandas as pd
import nltk
from nltk.corpus import stopwords

# Si esta activo el debug imprime los textos de debug
global debug_activado
debug_activado = 0

# GLOBALES
global const_peso_tristeza
const_peso_tristeza = -1.0

global const_peso_felicidad
const_peso_felicidad = 1.0

# Stopwords que se van a permitir
global stopwords_permitidas 
stopwords_permitidas = ('no')

# Camino a los ficheros IN y OUT dependiendo del entorno de desarrollo
# const_directorio_fichero = '/content/' # Para Colab
global const_directorio_fichero 
const_directorio_fichero = '' # Para VS Code

global vocabulario_pd 
vocabulario_pd = pd.DataFrame()

global spanish_stopwords
#
# Prepara la lista de stopwords españolas para usarla en cualquier momento que se necesite eliminar
#
# Tienes que descargarte las stopwords primero via nltk.download()
# Sólo la primera vez, al iniciar el entorno de Colab (la VM se borra al salir)
print ('*** Para cargar las stops words introducir: ***\n\nOpción d) -> stopwords -> q\n')
nltk.download('stopwords')
spanish_stopwords = stopwords.words('spanish')

global vocabulario_sin_stopwords

global vocabulario_base_pd
global vocabulario_stemmed_pd
global tweets_pd

global vocabulario_preparado
vocabulario_preparado = False
global valoracion_calculada
valoracion_calculada = 0.0

global palabras_encontradas
palabras_encontradas = []
global palabras_encontradas_lista
palabras_encontradas_lista = []
global palabras_encontradas_sospechosas
palabras_encontradas_sospechosas = []
global palabras_encontradas_sospechosas_resumen
palabras_encontradas_sospechosas_resumen = []
global palabras_encontradas_sospechosas_resumen_pd 
palabras_encontradas_sospechosas_resumen_pd = pd.DataFrame(columns=['Palabra_sospechosa', 'Apariciones'])