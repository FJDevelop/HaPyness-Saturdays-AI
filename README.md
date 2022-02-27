# HaPyness: ¿Aragón feliz?
 Saturdays AI - Zaragoza - Equipo 6
 
![image](https://user-images.githubusercontent.com/99982689/155894587-f627cbf4-6b5c-42f7-b607-f135725c60d4.png)


## La inspiración
> La contingencia sanitaria Covid-19 ha ocasionado circunstancias excepcionales con alto impacto en la sociedad, confinamiento masivo, soledad, incertidumbre, crisis económica, sanitaria y social, lo cual ha generado diferentes tipos de reacciones en la población, incrementando las patologías presentes tanto físicas como psíquicas, problemas económicos, entre otros. 

Algunos datos:
* 1 de cada 5 personas que han pasado Covid se ha enfrentado por primera vez a un diagnóstico de ansiedad, depresión o insomnio
* 1/3 personas adultas reportan niveles de angustia.1/2  en la población más joven. 
* 6,4% de la población ha acudido a un/a profesional de la salud mental desde que se inició la pandemia (más del doble fueron mujeres)
* 5,8% ha recibido tratamiento psicológico
* 8%-10% incremento de los pensamientos suicidas, especialmente en personas jóvenes. 

## Problema
> 
> Dada la situación de pandemia vivida a lo largo del último año queremos analizar cómo esta situación ha podido afectar a la percepción general a nivel psicológico de los ciudadanos de Aragón, y cómo ha podido influir este estado respecto a diferentes temáticas (inferidas o prefijadas) en sus comentarios en diferentes medios, redes sociales, prensa, etc.
>
> Existe una alta complejidad a la hora de realizar un análisis de sentimientos (etiquetado manual, tiempo, ambigüedad y alto riesgo de errores)


## Solución
> Objetivo 1: Brindar a la sociedad una herramienta que de un etiquetado automático y subsane la complejidad de un etiquetado manual, facilite la labor y reduzca la ambigüedad y el error.
Demostrar que la herramienta es viable y desarrollo de toda la metodología
>
> Objetivo 2: Desarrollar un modelo que analice la evolución del sentimiento de los ciudadanos en Aragón respecto a diferentes temáticas (inferidas o pre-fijadas), teniendo en cuenta redes sociales, prensa, etc. Y en función del análisis realizado realice recomendaciones. 
>


## Dataset
* Para el cálculo algorítmico de felicidad se han usado como referencia de contraste las valoraciones humanas del fichero TASS20_Datasets\Datasets\Task2\train.tsv
* Para el entrenamiento de la IA se han obtenido tweets relativos a Aragón, obtenidos con Tweepy filtrando por XYZ ---> Criterios de filtrado de Hector 
* Los resultados del cálculo algorítmico se han utilizado para entrenar la IA ---> indicar cómo se ha comparado la IA con el cálculo alhorítmico etc

## Modelos
* Random Forest
* SVM
* XGBoost

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

Ficheros de entrada (directorio **\IN**)  

![image](https://user-images.githubusercontent.com/99982689/154821701-b4575fb8-9ae8-40d2-b926-9e47b92b1a65.png)
* IN_FelizTriste.csv => Vovabulario previamente valorado en un excel  
 Está basado en 3000 palabras relacionadas con 'felicidad' y 'tristeza', obtenidas en http://www.ideasafines.com.ar/buscador-ideas-relacionadas.php
 Tras el postprocesado intensivo de las mismas y formateado, se ha ajustado el vocabulario a las 2600 palabras con la menor ambigüedad posible.  
 Las 3000 palabras han sido revisadas manualmente, para eliminar ambigüedades y errores de valoración.  
 
![image](https://user-images.githubusercontent.com/99982689/154821716-b3b1b7fa-0069-44a7-9c05-8a689fcabdb2.png)
* IN_train.csv => Tweets en csv. Puede proceder de:  
 El fichero TASS20_Datasets\Datasets\Task2\train.tsv (con valoración humana manual)
 El fichero obtenido de Tweepy, basado en contextos de Aragón (sin valoración humana) 

Ficheros de salida (directorio **\OUT**):

* OUT_FelizTriste_stemmed.csv =s contiene las raíces de "FelizTristeIN.csv", eliminado duplicadas.  
 Si se producen errores durante los cálculos es porque hay una misma raíz valorada con valores contradictorios
* OUT_es.csv => es_IN.csv pero con una columna adicional con la valoración calculada  
* OUT_es_errores.csv => tweets en los que la valoración del corpus y la calculada son diferentes
* OUT_es_sospechosas => Palabras sospechosas porque aparecen en tweets en los que la valoración calculada y la humana son diferentes

![image](https://user-images.githubusercontent.com/99982689/154821723-c0dfa5c3-5365-425d-9a54-9f0d458aea48.png)

Ficheros de imágenes: directorio **\IMG**

### Valoración de felicidad con IA

Ficheros Colab: directorio **\Colab**):

---> Completar
