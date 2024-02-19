"""
Definimos estructuras base para facilitar la verificación del código.
Sabemos que los comandos tendrán una estructura definida, así como las condiciones
(a excepción de RUN_DIRS, que puede tener una cantidad de direcciones indeterminada)
Las estructuras de control no se puede estandarizar, entonces serán verificadas individualmente.
"""

COMANDOS = [
    ['LP', 'DEFVAR', 'NAME', 'NUMBER', 'RP'],
    ['LP', '=', 'NAME', 'NUMBER', 'RP'],
    ['LP', 'MOVE', 'NUMBER', 'RP'],
    ['LP', 'SKIP', 'NUMBER', 'RP'],
    ['LP', 'TURN', 'D','RP'],
    ['LP', 'FACE', 'O', 'RP'],
    ['LP', 'PUT', 'X', 'NUMBER', 'RP'],
    ['LP', 'PICK', 'X', 'NUMBER', 'RP'],
    ['LP', 'MOVE-DIR', 'NUMBER', 'D', 'RP'],
    ['LP', 'MOVE-FACE', 'NUMBER', 'D', 'RP'],
    ['LP', 'NULL', 'RP'],
]

CONDICIONES = [
    ['LP', 'FACING?', 'O', 'RP']
    ['LP', 'BLOCKED?', 'RP']
    ['LP', 'CAN-PUT?', 'X', 'NUMBER', 'RP']
    ['LP', 'CAN-PICK?', 'X', 'NUMBER', 'RP']
    ['LP', 'CAN-MOVE?', 'O', 'RP'],
    ['LP', 'ISZERO?', 'NUMBER', 'RP']
    ['LP', 'NOT', 'CONDICION', 'RP']
]

"""
Se crea la pila para analizar el código, así como un contador que verficará
la concordancia de paréntesis emparejados. Adicionalmente se crea una lista
para guardar la posición de los parentésis izquierdos, esto con el fin de poder
vaciar la pila de manera más eficiente.
"""

stack = []
LPposition = []
contador = 0

"""
La función de verficación nos informará si el código es válido según nuestra gramática
Verificará constantemente la concordancia de paréntesis y de elementos individuales,
una vez identifique inconsistencias, el algorítmo dejará de funcionar y reportará que
el código ingresado es inválido.
También contempla la posibilidad de error por falta de paréntesis, entonces para esto
verificaremos que todas las instrucciones finales de la pila correspondan a comandos y
no a otro tipo de líneas.
"""

def verificacion(lista):

    flag = True

    for i in range(len(lista)):
        if flag == False:
            break

        tok = lista[i]
        stack.append(tok)
        print(stack)
        if tok == "LP":
            LPposition.append(i)
            contador+=1

        elif tok == "RP":
            lpN = LPposition.pop(-1)
            sublist = lista[lpN:i+1]
            contador -= 1
            
            if contador < 0:
                flag = False

            print("------")
            for j in range(i-lpN +1):
                if (len(stack) > 0):
                    h = stack.pop()
                    print(h)

            print("** " + str(sublist))

            corte = pertence(sublist)

            if (corte == None):
                flag = False
            
            else:
                stack.append(corte)
                print(stack)
    
    for elemento in stack:
        if elemento != 'COMANDO':
            flag = False
   
    return flag

"""
La función pertenece se encarga de evaluar cada subcadena (tokens contenidos entre dos paréntesis
emparejados) y de clasificarlos en categorias. Así sabremos si las condiciones, comandos y
estructuras de control tiene una sintáxis válida.
"""

def pertence(sublist):

    if sublist in CONDICIONES:
        return "CONDICION"
    
    elif sublist in COMANDOS:
        return 'COMANDO'
    
    elif sublist[1] == 'RUN-DIRS':
        longi_sub = len(sublist)
        centinela_sub = True
        
        if sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
            for i in range(2, longi_sub-2):
                if sublist[i] != 'D':
                    centinela_sub = False
        else:
            return None
        
        if centinela_sub == True:
            return 'COMANDO'
        
        else:
            return None
        
    elif sublist == ['LP', 'RP']:
        return 'PARAMS'
    
    elif sublist[1] == 'IF' and sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
        if sublist[2] == 'CONDICION':
            longi_sub = len(sublist)
            centinela_sub = True
            for i in range(3, longi_sub-2):
                if sublist[i] != 'COMANDO':
                    centinela_sub = False
        
        if centinela_sub == True:
            return 'COMANDO'
        
        else:
            return None
        
    elif sublist[1] == 'LOOP' and sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
        if sublist[2] == 'CONDICION':
            longi_sub = len(sublist)
            centinela_sub = True
            for i in range(3, longi_sub-2):
                if sublist[i] != 'COMANDO':
                    centinela_sub = False
        
        if centinela_sub == True:
            return 'COMANDO'
        
        else:
            return None
    
    elif sublist[1] == 'REPEAT' and sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
        if sublist[2] == 'NUMBER':
            longi_sub = len(sublist)
            centinela_sub = True
            for i in range(3, longi_sub-2):
                if sublist[i] != 'COMANDO':
                    centinela_sub = False
        
        if centinela_sub == True:
            return 'COMANDO'
        
        else:
            return None
        
    elif sublist[1] == 'DEFUN' and sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
        if sublist[2] == 'NAME' and sublist[3] == 'PARAMS':
            longi_sub = len(sublist)
            centinela_sub = True
            for i in range(4, longi_sub-2):
                if sublist[i] != 'COMANDO':
                    centinela_sub = False
        
        if centinela_sub == True:
            return 'COMANDO'
        
        else:
            return None
                
    elif sublist[0] == 'LP' and sublist[len(sublist)-1] == 'RP' and len(sublist) > 2:
        es_parametro = True
        for pos in range(1, len(sublist)-1):
            if sublist[pos] != 'NAME':
                es_parametro = False
        
        if es_parametro == True:
            return 'PARAMS'
        elif es_parametro == False:
            return None

    else:
        return None
    