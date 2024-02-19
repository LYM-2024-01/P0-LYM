
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



"""
La funcion dar_tipo recibe una palabra del archivo que previamente fue separada
LA funcion usa otras funciones auxiliares en donde reviza muchos casos haciendo
uso de constantesqe son listas.

Devuelte un ID, que le llamamos TOKEN por facilidad. 
"""
def dar_tipo(palabra):
    id = ""

    if (palabra == "("):
        id = "LP"

    elif (palabra == ")"):
        id = "RP"
    
    elif (es_numero(palabra)):
        id = "NUMBER"

    elif (es_condicion(palabra)):
        id = palabra.upper()

    elif (es_comando(palabra)):
        id = palabra.upper()

    elif (es_estructura(palabra)):
        id = palabra.upper()

    elif (es_cardinal(palabra)):
        id = "O"

    elif (es_giro(palabra)):
        id = "D"

    elif (es_item(palabra)):
        id = "X"

    elif (es_null(palabra)):
        id = "NULL"
 
    elif (es_constante(palabra)):
        id = "CONSTANTE"

    else: 
        if (palabra != ""):
            id = "NAME"

    return id




"""
La funcion siguiente_palabra recibe el archivo de texto y una posicion 
que es en donde se encuentra la ultima posicion revisada.

Se separa las palabras teniendo en cuenta que los separadores de las palabras son 
estacios ' ' y los parentesis '(' , ')'.
Cuando encuentra dichos separadores llama para cada iteración y decuelve la el TOKEN 
que le corresponda a la palabra, que obtiene al llamar a la funcion dar_tipo.  
o caracter importante como el caso de los parentesis.
tambien devuelve la posicion del archivo en la cual se quedo.
"""
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

    
    idp = dar_tipo(palabra)
             
    return idp, i  




"""
La función separar_texto toma como entrada un archivo de completo en formato de String
en minusculas y devuelve una lista con los Tokens y símbolos encontrados 
en el archivo.

Se utiliza un ciclo while que itera sobre las palabras en el archivo 
hasta que se han procesado todos los caracteres. 
Se llama a la funcion siguiente_palabra apenas se empieza.
LA funcion retorna la siguiente palabra o caracter que cuente como palabra 
en el archivo en forma de TOKEN. 

Se guardan los tokens en orden y se retorna una lista con dichos Tokens.
"""
def separar_texto (archivo):

    tamanio = len(archivo)
    respuesta = []
    i = 0
    while(i < tamanio):

        palabra, i = siguiente_palabra (archivo, i)
        
        if (palabra not in separadores):
            respuesta.append(palabra)
    
    return respuesta


