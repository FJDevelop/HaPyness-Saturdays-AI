###
#
# Bucle principal de streamlit. 
# Cuando se desea ejecutar la versión streamlit, se ejecuta prg_main_streamlit.py
# Cuando se desea valorar tweets en base al vocabulario, se ejecuta prg_main_calculo.py
#
# Para referencia de streamlit ver: https://docs.streamlit.io/library/api-reference
#
###

# Preparatorio streamlit: conda install streamlit 
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Tras ejecutar este módulo en VS Code, ejecutar en la línea de comandos para que se lance el Web explorer:
#   streamlit run "c:/Users/fjime/Google Drive/Principal/Fernando/Curso IA/Proyecto/Proyecto VS Code/prg_main_streamlit.py"

import prg_tweets as twe
import prg_globales as glb
import prg_pasos as pasos
import prg_auxiliares as aux
from PIL import Image

# Texto de los botones
const_boton_aragon_feliz = 'Ver felicidad en Aragón en los últimos años'
const_boton_ejemplo_1 = "▶️ Es una pena, cada vez hay menos felicidad :("
const_boton_ejemplo_2 = "▶️ Si me dices lo que piensas me das una alegría :)"
const_boton_ejemplo_3 = "▶️ Qué pena, NO me das una alegría :|"
const_boton_ejemplo_4 = "▶️ Sí es mejor que morirse :|"

const_color_verde = "#01A101"
const_color_rojo = "#C40202"
const_color_azul = "#0000FF"

# const_boton_ejemplo_5 = "▶️ Ejemplo 5: Estoy entristecido, apenado, pero a la vez feliz, contento :|"

#
# Funciones usadas en este módulo para la versión web con streamlit
#

#
# Según sea la valoración imprime con streamlit el estado de felicidad
#
def imprime_valoracion(valoracion):
    st.markdown("<body>Palabras encontradas: " + aux.dime_html_texto_color("<b>"+ glb.palabras_encontradas + "</b>", const_color_azul) + "</body>", unsafe_allow_html=True)
    if valoracion == 0:
        st.markdown("<body>Valoración calculada: " + aux.dime_html_texto_color("<b>estás indiferente</b>", const_color_azul) + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_indiferente.png", width = 75)
    elif valoracion == 1:
        st.markdown("<body>Valoración calculada: " + aux.dime_html_texto_color("<b>estás feliz</b>", const_color_verde) + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_feliz.png", width = 75)
    elif valoracion == -1:
        st.markdown("<body>Valoración calculada: " + aux.dime_html_texto_color("<b>estás triste</b>", const_color_rojo) + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_triste.png", width = 75)
    palabras_encontradas_lista_pd = pd.DataFrame(glb.palabras_encontradas_lista, columns = ["Raíz", "Valoración"])
    st.table(palabras_encontradas_lista_pd)
    st.markdown("Eliminados: emoticonos, hastag, menciones, abreviaturas, retweets, URL, símbolos, monedas...")

#
# Imprime el encabezado común a los dos procesos: preparar vocabulario y valorar tweets de forma interactiva
#
def imprime_encabezado():
    st.image("IMG\img_Saturdays_HaPyness.png", width=500)
    # st.write("https://saturdays.ai/") # Opcional
    st.title("HaPyness: ¿Aragón feliz?")
    st.header("Análisis automático de sentimientos")
    # st.subheader("--") # Info. Util si se desean más niveles de titulares

#
# Calcula la felicidad según el <texto> dado
#
def calcula_felicidad(texto):
    if glb.vocabulario_preparado:
        glb.valoracion_calculada, glb.palabras_encontradas, glb.palabras_encontradas_lista = twe.valora_tweet(glb.vocabulario_stemmed_pd, texto)
        imprime_valoracion(glb.valoracion_calculada)

#
# Atención: las variables globales han de estar fuera, porque la ejecución de streamlit es cíclica 
# Si se inicializan al principio del bucle, se inicializan en cada ciclo
# Ver aquí como itera streamlit: https://docs.streamlit.io/library/get-started/main-concepts#app-model 
#
def principal_streamlit():
    icon_image = Image.open('IMG\img_icono_HaPyness.png')  
    st.set_page_config(page_title='HaPyness: ¿Aragón feliz?', layout="wide", page_icon=icon_image) # layout = "centered", "wide"
    columna1, columna2, columna3 = st.columns(3)

    #
    # Si no se ha cargado y procesado el vocabulario, lo prepara
    #
    if not glb.vocabulario_preparado:
        with columna1:
            imprime_encabezado()

            if st.button('▶️ Preparar vocabulario'):
                st.markdown("<body><b>PASO 1: </b> " + aux.dime_html_texto_color("<b>Importando vocabulario...</b>", const_color_verde) + "</body>", unsafe_allow_html=True)
                pasos.PASO_1_importa_vocabulario()
                st.markdown("Hecho.")

                st.markdown("<body><b>PASO 2: </b>" + aux.dime_html_texto_color("<b>Analizando las 2600 palabras clave del vocabulario...</b>", const_color_verde) + "</body>", unsafe_allow_html=True)
                st.markdown("<body>Quitando stopwords y buscando las raíces en el vocabulario (stemmer)...</body>", unsafe_allow_html=True)
                st.markdown("")
                # st.markdown("<body>" + aux.dime_html_texto_color("<b>Analizando las 2600 palabras clave del vocabulario...</b>", const_color_verde) + "</body>", unsafe_allow_html=True)
                st.markdown("")
                st.image("IMG\img_pensando.png", width = 100)

                pasos.PASO_2_prepara_vocabulario()
                st.markdown("<body>Hecho. " + aux.dime_html_texto_color("<b>Vocabulario preparado.</b>", const_color_verde) + "</body>", unsafe_allow_html=True)
                st.markdown("")
                glb.vocabulario_preparado = True
                st.button('¿Eres feliz?')
                st.stop()
        with columna2:
            # st.markdown("<br><br>", unsafe_allow_html=True)
            st.image("IMG\img_ejemplo_vocabulario.gif") # No indicar width=400, porque no muestra el gif en bucle, sino una imagen fija)

        #
        # Si el vocabulario está cargado, muestra el campo con el tweet a valorar
        # Por defecto propone un texto, para hacer comprobaciones cuando se realizan cambios en el código
        #
        # Atención, streamlit ejecuta este bucle en orden secuencial, el else se ejecuta en el siguiente ciclo, 
        # cuando cambia un campo por interacción del usuario (!)
        #
    else:
        with columna1:
            imprime_encabezado()

            #st.subheader("¡Anímate a tweetear!")
            
            # Este botón fuerza el reinicio del formulario (al principio, antes de cargar el vocabulario), pero hay que darle dos veces
            # st.button("Reiniciar")

            # Introducción interactiva de un tweet
            with st.expander("¡Anímate a tweetear 👍! ¿Estás felíz 😀 o triste 😔?"):
                user_input = st.text_input("", "Ejemplo: Estoy entristecido, apenado, pero a la vez feliz, contento ⌨️ https://saturdays.ai/")

                if st.button("¿Feliz o triste?"):
                    calcula_felicidad(user_input)
        
            # Muestra algunos ejemplos para pruebas o demostraciones, con botones
            with st.expander("EJEMPLO 1"):
                if st.button(const_boton_ejemplo_1):
                    user_input = const_boton_ejemplo_1
                    calcula_felicidad(user_input)
            with st.expander("EJEMPLO 2"):
                if st.button(const_boton_ejemplo_2):
                    user_input = const_boton_ejemplo_2
                    calcula_felicidad(user_input)
            with st.expander("EJEMPLO 3"):
                if st.button(const_boton_ejemplo_3):
                    user_input = const_boton_ejemplo_3
                    calcula_felicidad(user_input)
            with st.expander("EJEMPLO 4"):
                if st.button(const_boton_ejemplo_4):
                    user_input = const_boton_ejemplo_4
                    calcula_felicidad(user_input)
            with st.expander("VOCABULARIO"):
                st.image("IMG\img_ejemplo_vocabulario.png") 
        with columna2:
            # st.markdown("<br><br>", unsafe_allow_html=True)
            st.image("IMG\img_ejemplo_tweets.png", width=640)
            if st.button('🔁 Reiniciar desde el principio'):
                glb.vocabulario_preparado = False
                st.stop()
        # Muestra algunos ejemplos para pruebas o demostraciones, texto para copiar y pegar
        # st.write("Ejemplo 1: Es una pena, cada vez hay menos felicidad :(")
        # st.write("Ejemplo 2: Si me dices lo que piensas me das una alegría :)")
        # st.write("Ejemplo 3: Sí es mejor que morirse :|")
        # st.write("Ejemplo 4: Que pena, no me das una alegría")

        # if const_boton_aragon_feliz not in st.session_state:
        #     felicidad_fechas_pd = glb.pd.read_csv("..\Colab\COLAB_por_fechas.csv", 
        #                         names = ['Fecha', 'valoracion_calculada', 'Covid', 'Numero_Tweets'], 
        #                         skiprows=1, delimiter=";", encoding='latin1', index_col=False)
        #     df6 = pd.DataFrame(felicidad_fechas_pd.value_counts()).reset_index()
        #     df6["Suma"]=df6[""]
        #     df6 = df6.sort_values(by ='Fecha')

        #     plt.figure(figsize =(10,3))
        #     sns.set_theme(context = 'talk')

        # if st.button(const_boton_aragon_feliz):
        #     st.write("    Tweets tristes y felices por años:")
        #     fig = px.line(x=df6['Fecha'], y=df6['Numero_Tweets'], color = df6['valoracion_calculada'],
        #         labels={
        #                 "y": "Número de tweets",
        #                 "x": "",
        #                 "color": "Valoración calculada"
        #             },)
        #     # fig = px.line(x=df6['Fecha'], y=df6['Numero_Tweets'],
        #     #     labels={
        #     #             "y": "Número de tweets",
        #     #             "x": "",
        #     #             "color": "Valoración calculada"
        #     #         },)
        #     st.plotly_chart(fig, use_container_width=True)
        #     print("Dibujando en streamlit")

#
# Ejecuta el bucle principal de streamlit
#
principal_streamlit()

# INFO AYUDA FORMATEADO WEB:
# icon_image = Image.open('/data/mcrodriguez/SaturdaysAI_ZGZ/eq_1_demanda_empleo/src/main/streamlit/icon_offer.png')  
#     st.set_page_config(page_title='Ofertas de Empleo en Aragón',
#                        page_icon=icon_image, # "🧊"
#                        layout="wide", # "centered", "wide"
#                        initial_sidebar_state="auto", # "expanded", "auto", "collapsed"
#                        menu_items= None # {'About': "# This is a header. This is an *extremely* cool app!"}