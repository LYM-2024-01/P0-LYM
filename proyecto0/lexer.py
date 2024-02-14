import pyparsing as pp





def separedo_texto (archivo):


    caracteres_importantes = ["(", ")"]
    separadores = ["(", ")", " ", "\n", "\t"]
    tamanio = len(archivo)
    respuesta = []
    i = 0

    while(i < tamanio):
        palabra = ""
        
        flag1 = True
        #print(archivo[i])
        while(flag1):
            if (archivo[i] not in separadores):
                palabra += archivo[i]
                i+=1
                #print(palabra)


            else:
                print("mal: " + str(i) + " " +archivo[i])
                flag1 = False

        if (palabra not in ["", " ", "\n", "\t"]):
            respuesta.append(palabra)
        i+=1
    
    print(respuesta)

