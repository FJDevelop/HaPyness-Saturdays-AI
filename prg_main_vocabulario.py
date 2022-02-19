import prg_pasos as pasos
import prg_globales as glb

def principal():

    pasos.PASO_1_importa_vocabulario()
    pasos.PASO_2_prepara_vocabulario()
    pasos.PASO_3_lee_tweets()
    pasos.PASO_4_valora_tweets()
    pasos.guarda_resultados()

    # Resumen
    num_errores = len(glb.errores_valoracion)
    num_tweets = glb.tweets_pd.shape[0]
    print ("\n*** RESUMEN ***\n")
    print ("Total errores: " + str(num_errores))
    print ("Total tweets: " + str(num_tweets))
    print ("Efectividad: " + str(int(100 * (1 - num_errores / num_tweets))) + "%\n")

# Cuando se ejecuta este módulo desde otro, comentar principal():
principal()