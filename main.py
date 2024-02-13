import sys
import pyparsing as pp
# pip install pyparsing



"""
integer  = Word(nums)            # simple unsigned integer
variable = Char(alphas)          # single letter variable, such as x, z, m, etc.
arith_op = one_of("+ - * /")      # arithmetic operators
equation = variable + "=" + integer + arith_op + integer    # will match "x=2+2", etc.
"""
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

instrucciones = {}






def end():
    sys.exit()


def main ():
    """
    while (True):
        linea = input()
        print(linea)

        flag = True
        while(flag):
    """       
    greet = pp.Word(pp.alphas) + "," + pp.Word(pp.alphas) + "!"
    for greeting_str in [
                "Hello, World!",
                "Bonjour, Monde!",
                "Hola, Mundo!",
                "Hallo, Welt!",
            ]:
        greeting = greet.parse_string(greeting_str)
        print(greeting)

if __name__ == '__main__':
    main()

