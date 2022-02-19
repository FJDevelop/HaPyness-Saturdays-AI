import prg_pasos as pasos
import prg_globales as glb
import prg_tweets as twe

def principal_test():

    pasos.PASO_1_importa_vocabulario()
    pasos.PASO_2_prepara_vocabulario()

# Cuando se ejecuta este módulo desde otro, comentar principal():
principal_test()
valoracion_calculada, palabras_encontradas, palabras_encontradas_lista = twe.valora_tweet(glb.vocabulario_stemmed_pd, 'que pena, no me das una alegría')
print ("Fin")