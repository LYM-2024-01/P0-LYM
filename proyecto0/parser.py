
constant = {
    "Dim" : "the dimensions of the board",
    "myXpos": "the x postition of the robot",
    "myYpos": "the y position of the robot",
    "myChips": "number of chips held by the robot",
    "myBalloons": "number of balloons held by the robot",
    "balloonsHere": "number of balloons in the robot’s cell",
    "ChipsHere": "number of chips that can be picked",
    "Spaces": "number of chips that can be dropped"
}

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

ESTRUCTURAS = [
    ['LP', 'IF', 'CONDICION', 'COMANDO', 'COMANDO', 'RP'],
    ['LP', 'LOOP', 'CONDICION', 'COMANDO', 'RP'],
    ['LP', 'REPEAT', 'NUMBER', 'COMANDO', 'RP'],
]


stack = []
LPposition = []
contador = 0

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
    
    if len(stack) != 0:
        flag = False

    
    return flag



    return True

def pertence(sublist):

    if sublist in CONDICIONES:
        return "CONDICION"
    
    elif sublist in COMANDOS:
        return 'COMANDO'
    
    elif sublist[1] == 'RUN-DIRS':
        longi_sub = len(sublist)
        centinela_sub = True
        
        if sublist[0] == 'LP' and sublist[longi_sub-1] == 'RP':
            for i in range(2, longi_sub-1):
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
                
                
    elif sublist[0] == 'LP' and sublist[len(sublist)-1] == 'RP' and len(sublist) > 2:
        es_parametro = True
        for pos in range(1, len(sublist)-1):
            if sublist[pos] != 'NAME':
                es_parametro = False
        
        if es_parametro == True:
            return 'PARAMS'
        elif es_parametro == False:
            return None
                
                
                
                
    
    #TODO Terminar con todos los posibles instrucciones y devolver el tipo si esta en el tipo

    else:
        return None
 
['LP', 'DEFUN', 'NAME', 'COMANDO', 'RP']
