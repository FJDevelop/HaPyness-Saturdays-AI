# HaPyness: ¿Aragón feliz?
 Saturdays AI - Felicidad o tristeza

## Breve resumen o descripción
---> Copiar los objetivos del ppt/artículo

## Dataset
* Para el cálculo algorítmico de felicidad se han usado como referencia las valoraciones humanas del fichero TASS20_Datasets\Datasets\Task2\train.tsv
* Para el entrenamiento de la IA se han obtenido tweets relativos a Aragón, obtenidos con Tweepy filtrando por XYZ ---> Criterios de filtrado de Hector 
* Los resultados del cálculo algorítmico se han utilizado para entrenar la IA ---> indicar cómo se ha comparado la IA con el cálculo alhorítmico etc

## Modelos
---> Indicar los modelos utilizados

## Ejemplos de uso


## Requirements

## Participantes 
Virginia Navarro  
Hector Soria  
Fernando Jiménez

## Próximos pasos

## Referencias
---> Copiar las referencias del artículo
---> Indicar referencia al TASS si es pública, o al menos la entidad que la gestiona

## Estructura del código

### Cálculo algorítmico de felicidad

Los módulos principales son los siguientes:

![image](https://user-images.githubusercontent.com/99982689/154820991-54aa7d1b-86bf-45b7-94d8-8100a6b4ae62.png)

* prg_auxiliares.py => Funciones auxiliares: debug y complementos
* prg_globales.py => Variables globales
* prg_main_calculo.py => Bucle principal de cálculo de valoraciones
* prg_main_streamlit.py => Bucle principal de streamlit  
 Cuando se desea ejecutar la versión streamlit, se ejecuta prg_main_streamlit.py  
 Cuando se desea valorar tweets en base al vocabulario, se ejecuta prg_main_calculo.py  
* prg_pasos.py => Pasos realizados para el cálculo automático de felicidad (pasos 1 a 4)  
 Para la parte interactiva de streamlit sólo se ejecutan los pasos 1 y 2
* prg_stemmer.py => Funciones relativas al stemmer de palabras y del vocabulario en csv
* prg_tweets.py => Funciones relativas a la limpieza/preparación y valoración automática de tweets

PASO 1: Importar el vocabulario
PASO 2: Prepara vocabulario stemmed (vocabulario_stemmed_pd)
PASO 3: Lee los tweets del csv
PASO 4: Valora tweets del csv

Ficheros de entrada:  
* IN_FelizTriste.csv => Vovabulario previamente valorado en un excel  
 Está basado en 3000 palabras relacionadas con 'felicidad' y 'tristeza', obtenidas en http://www.ideasafines.com.ar/buscador-ideas-relacionadas.php
 Tras el postprocesado intensivo de las mismas y formateado, se ha ajustado el vocabulario a las 2600 palabras con la menor ambigüedad posible.  
 Las 3000 palabras han sido revisadas manualmente, para eliminar ambigüedades y errores de valoración.  
* IN_es.csv => Tweets en csv. Puede proceder de:  
 El fichero TASS20_Datasets\Datasets\Task2\train.tsv (con valoración humana manual)
 El fichero obtenido de Tweepy, basado en contextos de Aragón (sin valoración humana) 

Ficheros de salida:
* OUT_FelizTriste_stemmed.csv =s contiene las raíces de "FelizTristeIN.csv", eliminado duplicadas.  
 Si se producen errores durante los cálculos es porque hay una misma raíz valorada con valores contradictorios
* OUT_es.csv => es_IN.csv pero con una columna adicional con la valoración calculada  
* OUT_es_errores.csv => tweets en los que la valoración del corpus y la calculada son diferentes
* OUT_es_sospechosas => Palabras sospechosas porque aparecen en tweets en los que la valoración calculada y la humana son diferentes




