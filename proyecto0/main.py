import sys
import pyparsing as pp
import lexer
# pip install pyparsing






def end():
    sys.exit()


def main ():
     
    ruta_archivo=input("Ingrese la ruta del archivo ( por ejemplo: proyecto0/documentos/ejemplo2.txt): ")
    archivo= open(ruta_archivo).read().lower()

    lexer.separedo_texto(archivo)


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

    """

if __name__ == '__main__':
    main()

