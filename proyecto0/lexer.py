import token as tk 


caracteres_importantes = ["(", ")"]
separadores = ["", " ", "\n", "\t"]



NUMEROS = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

CONSTANTES = ["dim", "myxpos", "myypos", "mychips", "myballoons", "balloonshere", "chipsHere", "spaces"]

O = [":north", ":south", ":east", ":west"]

D = [":left", ":right", ":around", ":front", ":back", ":up", ":down"]

X = [":balloons", ":chips"]

NULL = ["null"]



SUBCOMANDOS = ["defvar", "move", "skip", "turn", "face", "put", "pick", "move-dir", "run-dirs", "move-face", "null"]

SUBESTRUCTURA = ['if', 'loop', 'repeat', 'defun']

SUBCONDICIONES = ['facing?', 'blocked?','can-put?', 'can-pick?', 'can-move?', 'iszero?', 'not']





def es_numero (palabra):
    flag = True
    if (len(palabra) > 0):
        for i in range(len(palabra)):
            if (palabra[i] not in NUMEROS):
                flag = False
    else:
        flag = False
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

def es_estructura (palabra):
    flag = True
    if (palabra not in SUBESTRUCTURA):
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


def es_item (palabra):
    flag = True
    if (palabra not in X):
        flag = False
    return flag

def es_null (palabra):
    flag = True
    if (palabra not in NULL):
        flag = False
    return flag

def es_constante (palabra):
    flag = True
    if (palabra not in CONSTANTES):
        flag = False
    return flag



def dar_tipo(palabra):
    id = ""
    valor = ""

    if (palabra == "("):
        id = "LP"
        valor="(" 

    elif (palabra == ")"):
        id = "RP"
        valor=")" 
    
    elif (es_numero(palabra)):
        id = "NUMBER"
        valor = palabra

    elif (es_condicion(palabra)):
        id = palabra.upper()
        valor = palabra

    elif (es_comando(palabra)):
        id = palabra.upper()
        valor = palabra

    elif (es_estructura(palabra)):
        id = palabra.upper()
        valor = palabra

    elif (es_cardinal(palabra)):
        id = "O"
        valor = palabra

    elif (es_giro(palabra)):
        id = "D"
        valor = palabra

    elif (es_item(palabra)):
        id = "X"
        valor = palabra

    elif (es_null(palabra)):
        id = "NULL"
        valor = palabra
 
    elif (es_constante(palabra)):
        id = "CONSTANTE"
        valor = palabra

    else: 
        if (palabra != ""):
            id = "NAME"
            valor = palabra

    return id, valor



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

    
    idp, valorp = dar_tipo(palabra)

    adicion = tk.Token(idp, valorp)
    return adicion, i               # return idp, i   #Cambiar el return de adicion por el de idp y el comentario de mas abajo para imprimir





def separar_texto (archivo):

    tamanio = len(archivo)
    respuesta = []
    i = 0
    while(i < tamanio):

        palabra, i = siguiente_palabra (archivo, i)
        
        if (palabra not in separadores):
            respuesta.append(palabra)
    
    return respuesta





archivo= open("proyecto0/documentos/ejemplo.txt").read().lower()

lista = separar_texto(archivo)
#print(lista)            #Quitar comentario para imprimir lista

