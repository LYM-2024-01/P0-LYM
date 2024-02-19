
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
    ['LP', 'RP'],
    ['LP', 'MOVE', 'NUMBER', 'RP'],
    ['LP', 'SKIP', 'NUMBER', 'RP'],
    ['LP', 'TURN', 'D','RP'],
    ['LP', 'FACE', 'O', 'RP'],
    ['LP', 'PUT', 'X', 'NUMBER', 'RP'],
    ['LP', 'PICK', 'X', 'NUMBER', 'RP'],
    ['LP', 'MOVE-DIR', 'NUMBER', 'D', 'RP'],
    ['LP', 'RUN-DIRS', '', 'RP'],
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
    ['LP', 'DEFUN', 'NAME', 'COMANDO', 'RP']
]


stack = []
LPposition = []

def verificacion(lista):

    flag = True

    for i in range(len(lista)):

        tok = lista[i]
        stack.append(tok)
        print(stack)
        if tok == "LP":
            LPposition.append(i)


        elif tok == "RP":
            lpN = LPposition.pop(-1)
            sublist = lista[lpN:i+1]

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

        

    
    return flag



    return True





def pertence(sublist):

    if sublist in CONDICIONES:
        return "CONDICION"
    

    #TODO Terminar con todos los posibles instrucciones y devolver el tipo si esta en el tipo

    else:
        return None
 