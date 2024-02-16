import token as tk 


caracteres_importantes = ["(", ")"]
separadores = ["", " ", "\n", "\t"]



NUMEROS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

CONSTANTES = ["Dim", "myXpos", "myYpos", "myChips", "myBalloons", "balloonsHere", "ChipsHere", "Spaces"]

O = [":north", ":south", ":east", ":west"]

D = [":left", ":right", ":around"]

X = [":balloons", ":chips"]

DS = [":front", ":right", ":left", ":back"]

NULL = ["null"]



SUBCOMANDOS = ["defvar", "move", "skip", "turn", "face", "put", "pick", "move-dir", "run-dirs", "move-face", "null"]

SUBESTRUCTURA = ['if', 'loop', 'repeat', 'defun']

SUBCONDICIONES = ['facing?', 'blocked?','can-put?', 'can-pick?', 'can-move?', 'isZero?', 'not']





def es_numero (palabra):
    flag = True
    if (len(palabra) > 0):
        for i in range(len(palabra)):
            if (palabra[i] not in NUMEROS):
                flag = False
    else:
        flag = False
    print("Mirar palabra: " + palabra + " cond- " + str(flag))
    return flag

def es_condicion (palabra):
    flag = True
    if (palabra not in SUBCONDICIONES):
        flag = False
    return flag

def es_comando (palabra):
    flag = True
    if (palabra not in SUBCOMANDOS):
        flag = False
    return flag

def es_cardinal (palabra):
    flag = True
    if (palabra not in O):
        flag = False
    return flag

def es_giro (palabra):
    flag = True
    if (palabra not in D):
        flag = False
    return flag

def es_direccion (palabra):
    flag = True
    if (palabra not in DS):
        flag = False
    return flag

def es_item (palabra):
    flag = True
    if (palabra not in X):
        flag = False
    return flag

def es_null (palabra):
    flag = True
    if (palabra not in SUBESTRUCTURA):
        flag = False
    return flag


def siguiente_palabra (archivo, i):
    
    adicion = tk.Token("", "")
    palabra = ""
    flag1 = True
    while(flag1):

        if (archivo[i] in caracteres_importantes):
            palabra = archivo[i]
            if (archivo[i] == "("):
                adicion = tk.Token("LP","(")
            elif (archivo[i] == ")"):
                adicion = tk.Token("RP",")")
            flag1 = False


        elif (archivo[i] not in separadores) :
            palabra += archivo[i]
            #adicion = tk.Token(palabra,palabra)
            #print(adicion.valor)
            if(archivo[i+1] in caracteres_importantes):
                adicion = tk.Token(palabra,palabra)
                #print(" -- " + adicion.valor)
                flag1 = False


        else:
            if (es_numero(palabra)):
                adicion = tk.Token("NUMBER",palabra)
                print("Number "+palabra)

            elif (es_condicion(palabra)):
                adicion = tk.Token("CONDICION",palabra)

            elif (es_comando(palabra)):
                adicion = tk.Token("COMANDO",palabra)

            elif (es_cardinal(palabra)):
                adicion = tk.Token("DIRECCION",palabra)

            else: 
                if (palabra != ""):
                    adicion = tk.Token(palabra,palabra)
            print(" ** " + adicion.valor)
            flag1 = False
        i+=1
    #print(adicion.id)

    return adicion.id, i





def separar_texto (archivo):

    tamanio = len(archivo)
    respuesta = []
    i = 0
    while(i < tamanio):

        palabra, i = siguiente_palabra (archivo, i)
        
        if (palabra not in separadores):
            respuesta.append(palabra)
    
    return respuesta





#ruta_archivo=input("Ingrese la ruta del archivo ( por ejemplo: proyecto0/documentos/ejemplo2.txt): ")
archivo= open("proyecto0/documentos/ejemplo.txt").read().lower()

lista = separar_texto(archivo)
print(lista)

