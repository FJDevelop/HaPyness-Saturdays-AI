# Preparatorio streamlit: conda install streamlit 
import streamlit as st
import pandas as pd
import seaborn as sns

import plotly.express as px

# Tras ejecutar este módulo en VS Code, ejecutar en la línea de comandos para que se lance el Web explorer:
#   streamlit run "c:/Users/fjime/Google Drive/Principal/Fernando/Curso IA/Proyecto/Proyecto VS Code/prg_main_streamlit.py"

import prg_tweets as twe
import prg_globales as glb
import prg_pasos as pasos
from PIL import Image

def principal_streamlit():
    icon_image = Image.open('IMG\img_icono_HaPyness.png')  
    st.set_page_config(page_title='HaPyness: ¿Aragón feliz?', layout="centered", page_icon=icon_image) # layout = "centered", "wide"

    st.image("IMG\img_Saturdays_HaPyness.png")
    # st.write("https://saturdays.ai/") # Opcional
    st.title("HaPyness: ¿Aragón feliz?")
    st.header("Análisis automático de sentimientos")
    # st.subheader("--") # Info

    if "Ver gráficas" not in st.session_state:
        felicidad_fechas_pd = glb.pd.read_csv("Colab\COLAB_por_fechas.csv", 
                            names = ['Fecha', 'valoracion_calculada', 'Covid', 'Numero_Tweets'], 
                            skiprows=1, delimiter=";", encoding='latin1', index_col=False)
        df6 = pd.DataFrame(felicidad_fechas_pd.value_counts()).reset_index()
        df6 = df6.sort_values(by ='Fecha')

        # plt.figure(figsize =(10,3))
        # plt.show
        # sns.set_theme(context = 'talk')
    # else:
    if st.button('Ver gráficas'):
        # fig = px.line(x=df6['Fecha'], y=df6['Numero_Tweets'], color = df6['valoracion_calculada'],
        #       labels={
        #              "y": "Número de tweets",
        #              "x": "",
        #              "color": "Valoración calculada"
        #          },)
        # st.plotly_chart(fig, use_container_width=True)

        df7 = df6.groupby('Fecha').sum().reset_index()
        df7 #El sumatorio de tweets por año
        
        import plotly.express as px
        import plotly.graph_objects as go
        fig1 = px.line(x=df6['Fecha'], y=df6['Numero_Tweets'],color = df6['valoracion_calculada'],
        labels={
        "y": "Número de tweets",
        "x": "",
        "color": "Valoración calculada"
        })
        fig1.add_scatter(x=df7['Fecha'], y=df7['Numero_Tweets'], mode='lines', name = 'Suma')
        fig1.show()
        # fig = px.bar(df6, x='Fecha', y='Numero_Tweets', color='valoracion_calculada', title="Valoraciones de felicidad y tristeza por años")
        # fig.update_layout(barmode="stack")
        # fig.show()
        print("XXX")

#
# Ejecuta el bucle principal de streamlit
#
principal_streamlit()





#         a = sns.lineplot(data = df6, x = 'Fecha', y = 'Numero_Tweets', hue = 'valoracion_calculada', 
#                         ci = 0.95,palette = 'Set1')
# #        plt.setp(a, xticks = ('2007','2010', '2013','2016','2019', '2022'))
#         sns.move_legend(a, "upper right", bbox_to_anchor=(.75, 1), title='Valoracion calculada', frameon = False)
#         a.set(ylabel = 'Número de tweets', xlabel = '')
#         print("XXX")