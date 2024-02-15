import pyparsing as pp

caracteres_importantes = ["(", ")"]
separadores = [" ", "\n", "\t"]



def siguiente_palabra (archivo, i):
    
    palabra = ""
    flag1 = True
    while(flag1):

        if (archivo[i] in caracteres_importantes):
            palabra = archivo[i]
            flag1 = False

        elif (archivo[i] not in separadores) :
            palabra += archivo[i]

            if(archivo[i+1] in caracteres_importantes):
                flag1 = False

        else:
            flag1 = False
        i+=1

    return palabra, i




def separar_texto (archivo):

    tamanio = len(archivo)
    respuesta = []
    i = 0

    while(i < tamanio):

        palabra, i = siguiente_palabra (archivo, i)
        
        if (palabra not in separadores):
            respuesta.append(palabra)
    
    return respuesta

