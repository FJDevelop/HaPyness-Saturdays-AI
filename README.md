# HaPyness: ¿Aragón feliz?
 Saturdays AI - Zaragoza - Equipo 6
 
![image](https://user-images.githubusercontent.com/99982689/154822111-34f89283-5cbd-4304-a4e7-7bb896a4757f.png)

## Breve resumen o descripción
---> Copiar los objetivos del ppt/artículo

## Dataset
* Para el cálculo algorítmico de felicidad se han usado como referencia de contraste las valoraciones humanas del fichero TASS20_Datasets\Datasets\Task2\train.tsv
* Para el entrenamiento de la IA se han obtenido tweets relativos a Aragón, obtenidos con Tweepy filtrando por XYZ ---> Criterios de filtrado de Hector 
* Los resultados del cálculo algorítmico se han utilizado para entrenar la IA ---> indicar cómo se ha comparado la IA con el cálculo alhorítmico etc

## Modelos
---> Indicar los modelos utilizados

## Ejemplos de uso

## Requirements
> Google Colab
> Visual Studio Code
> Conda
> Streamlit
> Ficheros de entrada para el vocabulario y los tweets (ver más adelante)

## Participantes 
Virginia Navarro  
Hector Soria  
Fernando Jiménez

## Próximos pasos

En cuanto a la versión automática, mediante los fichero de salida (OUT_es_*) se puede: analizar las palabras sospechosas de generar fallos generales respecto a los tweets del DASS, analizar el impacto de las diferentes palabras del vocabulario en los errores de valoración de cada tweet, revisar la precisión del stemmer, y obtener la comparación entre la valoración humana del TASS con la valoración automática (ver ficheros de salida más abajo) 

Con todos estos ficheros se podría:
* Realizar más ajustes en el vocabulario de entrada. Esto exige de numerosas pruebas (y tiempo de proceso)  
* Ajustar el stemmer, para no considerar palabras confusas, se podría incluso probar la efectividad de otros stemmer  
* Someter el cálculo automático a tweets de otras versiones del TASS que ofrecen valoración humana, ajustando el vocabulario nuevamente para cubrir el máximos de TASS valorados humanos  

## Referencias
---> Copiar las referencias del artículo
---> Indicar referencia al TASS si es pública, o al menos la entidad que la gestiona

## Estructura del código

### Valoración automática de felicidad

Los módulos principales son los siguientes:

![image](https://user-images.githubusercontent.com/99982689/154820991-54aa7d1b-86bf-45b7-94d8-8100a6b4ae62.png)

* prg_auxiliares.py => Funciones auxiliares: debug y complementos
* prg_globales.py => Variables globales
* prg_main_calculo.py => Bucle principal de cálculo de valoraciones  
  Cuando se desea valorar tweets en base al vocabulario, se ejecuta prg_main_calculo.py  
* prg_main_streamlit.py => Bucle principal de streamlit  
  
  Cuando se desea ejecutar la versión streamlit, se ejecuta prg_main_streamlit.py  
  Al finalizar la ejecución muestra el comando a ejecutar para que streamlit aparezca en el explorador web:  
  > streamlit run "c:\[...]\HaPyness\prg_main_streamlit.py"  
  
  También puede lanzarse manualmente en:  
  > http://localhost:8501/
 
* prg_pasos.py => Pasos realizados para el cálculo automático de felicidad (pasos 1 a 4)  
 Para la parte interactiva de streamlit sólo se ejecutan los pasos 1 y 2  
 
  > PASO 1: Importar el vocabulario  
  > PASO 2: Prepara vocabulario stemmed
![image](https://user-images.githubusercontent.com/99982689/154822546-87e17b04-1903-41a2-8783-090e90cde1cb.png)

  > PASO 3: Lee los tweets del csv  
  > PASO 4: Valora tweets del csv  
![image](https://user-images.githubusercontent.com/99982689/154822587-f3468882-d3ae-4597-960a-8fc41054dcba.png)

* prg_stemmer.py => Funciones relativas al stemmer de palabras y del vocabulario en csv
* prg_tweets.py => Funciones relativas a la limpieza/preparación y valoración automática de tweets

Ficheros de entrada:  

![image](https://user-images.githubusercontent.com/99982689/154821701-b4575fb8-9ae8-40d2-b926-9e47b92b1a65.png)
* IN_FelizTriste.csv => Vovabulario previamente valorado en un excel  
 Está basado en 3000 palabras relacionadas con 'felicidad' y 'tristeza', obtenidas en http://www.ideasafines.com.ar/buscador-ideas-relacionadas.php
 Tras el postprocesado intensivo de las mismas y formateado, se ha ajustado el vocabulario a las 2600 palabras con la menor ambigüedad posible.  
 Las 3000 palabras han sido revisadas manualmente, para eliminar ambigüedades y errores de valoración.  
 
![image](https://user-images.githubusercontent.com/99982689/154821716-b3b1b7fa-0069-44a7-9c05-8a689fcabdb2.png)
* IN_train.csv => Tweets en csv. Puede proceder de:  
 El fichero TASS20_Datasets\Datasets\Task2\train.tsv (con valoración humana manual)
 El fichero obtenido de Tweepy, basado en contextos de Aragón (sin valoración humana) 

Ficheros de salida:

* OUT_FelizTriste_stemmed.csv =s contiene las raíces de "FelizTristeIN.csv", eliminado duplicadas.  
 Si se producen errores durante los cálculos es porque hay una misma raíz valorada con valores contradictorios
* OUT_es.csv => es_IN.csv pero con una columna adicional con la valoración calculada  
* OUT_es_errores.csv => tweets en los que la valoración del corpus y la calculada son diferentes
* OUT_es_sospechosas => Palabras sospechosas porque aparecen en tweets en los que la valoración calculada y la humana son diferentes

![image](https://user-images.githubusercontent.com/99982689/154821723-c0dfa5c3-5365-425d-9a54-9f0d458aea48.png)

### Valoración de felicidad con IA

---> Completar
