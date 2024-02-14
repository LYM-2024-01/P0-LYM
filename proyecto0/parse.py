


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

instrucciones = {"defvar": 2,
                 "move": 1, 
                 "skip": 1, 
                 "turn": 1, 
                 "face": 1,
                 "put": 2,
                 "pick": 2,
                 "move-dir": 2,
                 "run-dirs": 1,
                 "move-face": 2,
                 "null": 0,}

estructuras = {'if': 3,
               'loop': 2}

#agregar defun

condiciones = {'facing': 1,
               'blocked': 0,
               'can-put': 2,
               'can-pick': 2,
               'can-move': 1,
               'isZero': 1,
               'not': 1}

