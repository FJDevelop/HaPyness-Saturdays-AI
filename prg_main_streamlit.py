#
# Imports e instalación en conda de las librerias necesarias
#

# Preparatorio streamlit: conda install streamlit 
import streamlit as st
import pandas as pd

# Tras ejecutar este módulo en VS Code, ejecutar en la línea de comandos para que se lance el Web explorer:
#   streamlit run "c:/Users/fjime/Google Drive/Principal/Fernando/Curso IA/Proyecto/Proyecto VS Code/prg_main_streamlit.py"

import prg_tweets as twe
import prg_globales as glb
import prg_pasos as pasos
from PIL import Image

#
# Funciones usadas en este módulo para la versión web con streamlit
#
def imprime_valoracion(valoracion):
    if valoracion == 0:
        st.text("Valoración calculada: estás neutro")
    elif valoracion == 1:
       st.text("Valoración calculada: estás feliz")
    elif valoracion == -1:
       st.text("Valoración calculada: estás triste")
    st.write(glb.palabras_encontradas)
    palabras_encontradas_lista_pd = pd.DataFrame(glb.palabras_encontradas_lista, columns = ["Raíz", "Valoración"])
    st.table(palabras_encontradas_lista_pd)

def calcula_felicidad(texto):
    if glb.vocabulario_preparado:
        st.text("Eliminados: emoticonos, hastag, menciones, abreviaturas, retweets, URL, links, símbolos, monedas...")
        glb.valoracion_calculada, glb.palabras_encontradas, glb.palabras_encontradas_lista = twe.valora_tweet(glb.vocabulario_stemmed_pd, texto)
        imprime_valoracion(glb.valoracion_calculada)

#
# Atención: las variables globales han de estar fuera, porque la ejecución de streamlit es cíclica 
# y si se inicializan al principio, se inicializan en cada ciclo
# Ver aquí como itera streamlit: https://docs.streamlit.io/library/get-started/main-concepts#app-model 
#
def principal_streamlit():
    icon_image = Image.open('img_icono_HaPyness.png')  
    st.set_page_config(page_title='Ofertas de Empleo en Aragón', layout="centered", page_icon=icon_image) # layout = "centered", "wide"

    st.image("img_Saturdays_HaPyness.png")
    # st.write("https://saturdays.ai/")
    st.title("HaPyness: ¿Aragón feliz?")
    st.header("Análisis algorítmico de sentimientos")
    # st.subheader("---")

    #
    # Si no se ha cargado y procesado el vocabulario, lo prepar
    #
    if not glb.vocabulario_preparado:
        if st.button('Preparar vocabulario'):
            st.text("Estado: PASO 1: Importando vocabulario...")
            pasos.PASO_1_importa_vocabulario()
            st.text("Hecho.")

            st.text("Estado: PASO 2: Preparando vocabulario...")
            st.text("Quitando stopwords, buscando las raíces (stemmer)...")
            pasos.PASO_2_prepara_vocabulario()
            st.text("Hecho.")
            
            st.text("Estado: Vocabulario preparado.")

            glb.vocabulario_preparado = True
            st.button('¿Eres feliz?')
            st.stop()
    #
    # Si el vocabulario está cargado, muestra el campo con el tweet a valorar
    #
    # Atención, streamlit ejecuta en orden secuencial, el else se ejecuta en el siguiente ciclo, 
    # cuando cambia un campo por interacción del usuario!!!
    #
    else:
        st.subheader("¡Anímate a tweetear!")
        user_input = st.text_input("", "Estoy entristecido, apenado, pero a la vez feliz, contento")

        if st.button('¿Feliz o triste'):
            calcula_felicidad(user_input)

        st.write("Ejemplo 1: Es una pena, cada vez hay menos felicidad :(")
        st.write("Ejemplo 2: Si me dices lo que piensas me das una alegría :)")
        st.write("Ejemplo 3: Sí es mejor que morirse :|")
        st.write("Ejemplo 4: Que pena, no me das una alegría :(")

principal_streamlit()

# INFO AYUDA FORMATEADO WEB:
# icon_image = Image.open('/data/mcrodriguez/SaturdaysAI_ZGZ/eq_1_demanda_empleo/src/main/streamlit/icon_offer.png')  
#     st.set_page_config(page_title='Ofertas de Empleo en Aragón',
#                        page_icon=icon_image, # "🧊"
#                        layout="wide", # "centered", "wide"
#                        initial_sidebar_state="auto", # "expanded", "auto", "collapsed"
#                        menu_items= None # {'About': "# This is a header. This is an *extremely* cool app!"}