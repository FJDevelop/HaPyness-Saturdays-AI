###
#
# Bucle principal de streamlit. 
# Cuando se desea ejecutar la versión streamlit, se ejecuta prg_main_streamlit.py
# Cuando se desea valorar tweets en base al vocabulario, se ejecuta prg_main_calculo.py
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
from PIL import Image

# Texto de los botones
const_boton_aragon_feliz = 'Ver felicidad en Aragón en los últimos años'
const_boton_ejemplo_1 = "Ejemplo 1: Estoy entristecido, apenado, pero a la vez feliz, contento"
const_boton_ejemplo_2 = "Ejemplo 2: Es una pena, cada vez hay menos felicidad :("
const_boton_ejemplo_3 = "Ejemplo 5: Que pena, no me das una alegría :|"
const_boton_ejemplo_4 = "Ejemplo 4: Sí es mejor que morirse :|"
const_boton_ejemplo_5 = "Ejemplo 3: Si me dices lo que piensas me das una alegría :)"

#
# Funciones usadas en este módulo para la versión web con streamlit
#

def dime_html_texto_color(texto, color):
    return "<span style=""color:" + color + ">" + texto + "</span>"

#
# Según sea la valoración imprime con streamlit el estado de felicidad
#
def imprime_valoracion(valoracion):
    if valoracion == 0:
        # st.write("Valoración calculada: estás indiferente")
        st.markdown("<body>Valoración calculada: " + dime_html_texto_color("estás indiferente", "#0000FF") + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_indiferente.png", width = 50)
    elif valoracion == 1:
        # st.write("Valoración calculada: estás feliz")
        st.markdown("<body>Valoración calculada: " + dime_html_texto_color("estás feliz", "#01A101") + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_feliz.png", width = 50)
    elif valoracion == -1:
        # st.write("Valoración calculada: estás triste")
        st.markdown("<body>Valoración calculada: " + dime_html_texto_color("estás triste", "#C40202") + "</body>", unsafe_allow_html=True)
        st.image("IMG\img_triste.png", width = 50)
    # st.write(glb.palabras_encontradas) # Opcional, sólo para ver la versión textual y depurar
    palabras_encontradas_lista_pd = pd.DataFrame(glb.palabras_encontradas_lista, columns = ["Raíz", "Valoración"])
    st.table(palabras_encontradas_lista_pd)
    st.markdown("Eliminados: emoticonos, hastag, menciones, abreviaturas, retweets, URL, símbolos, monedas...")

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
    st.set_page_config(page_title='HaPyness: ¿Aragón feliz?', layout="centered", page_icon=icon_image) # layout = "centered", "wide"

    st.image("IMG\img_Saturdays_HaPyness.png", width=650)
    # st.write("https://saturdays.ai/") # Opcional
    st.title("HaPyness: ¿Aragón feliz?")
    st.header("Análisis automático de sentimientos")
    # st.subheader("--") # Info. Util si se desean más niveles de titulares

    #
    # Si no se ha cargado y procesado el vocabulario, lo prepara
    #
    if not glb.vocabulario_preparado:
        if st.button('Preparar vocabulario'):
            # st.text("Estado: PASO 1: Importando vocabulario...")
            st.markdown("<body>Estado: PASO 1: " + dime_html_texto_color("Importando vocabulario...", "#01A101") + "</body>", unsafe_allow_html=True)
            pasos.PASO_1_importa_vocabulario()
            st.text("Hecho.")

            # st.text("Estado: PASO 2: ...")
            st.markdown("<body>Estado: PASO 2: " + dime_html_texto_color("Preparando vocabulario...", "#01A101") + "</body>", unsafe_allow_html=True)
            st.markdown("Quitando stopwords, buscando las raíces (stemmer)...")
            st.image("IMG\img_pensando.png", width = 100)

            pasos.PASO_2_prepara_vocabulario()
            st.markdown("<body>Hecho. " + dime_html_texto_color("Vocabulario preparado.", "#01A101") + "</body>", unsafe_allow_html=True)

            glb.vocabulario_preparado = True
            st.button('¿Eres feliz?')
            st.stop()
    #
    # Si el vocabulario está cargado, muestra el campo con el tweet a valorar
    # Por defecto propone un texto, para hacer comprobaciones cuando se realizan cambios en el código
    #
    # Atención, streamlit ejecuta este bucle en orden secuencial, el else se ejecuta en el siguiente ciclo, 
    # cuando cambia un campo por interacción del usuario (!)
    #
    else:
        st.subheader("¡Anímate a tweetear!")
        user_input = st.text_input("", "Ejemplo 1: Estoy entristecido, apenado, pero a la vez feliz, contento")

        if st.button("¿Feliz o triste?"):
            calcula_felicidad(user_input)
 
        # Este botón fuerza el reinicio del formulario
        st.button("Reiniciar")
        st.image("IMG\img_linea_horizontal.png")

         # Muestra algunos ejemplos para pruebas o demostraciones, con botones
        if st.button(const_boton_ejemplo_1):
            user_input = const_boton_ejemplo_1
            calcula_felicidad(user_input)
        if st.button(const_boton_ejemplo_2):
            user_input = const_boton_ejemplo_2
            calcula_felicidad(user_input)
        if st.button(const_boton_ejemplo_3):
            user_input = const_boton_ejemplo_3
            calcula_felicidad(user_input)
        if st.button(const_boton_ejemplo_4):
            user_input = const_boton_ejemplo_4
            calcula_felicidad(user_input)
        if st.button(const_boton_ejemplo_5):
            user_input = const_boton_ejemplo_5
            calcula_felicidad(user_input)

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