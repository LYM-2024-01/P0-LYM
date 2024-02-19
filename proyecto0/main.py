import sys
import lexer
import proyecto0.parser as parser
# pip install pyparsing






def end():
    sys.exit()


def main ():
     
    ruta_archivo=input("Ingrese la ruta del archivo ( por ejemplo: proyecto0/documentos/ejemplo2.txt): ")
    archivo= open(ruta_archivo).read().lower()

    lista = lexer.separar_texto(archivo)
    print(lista)

    aceptado = parser.verificacion(lista)

    try:
        print("La cadena es válida según la gramática")

        #TODO Meter aca el llamado  aceptado = parse.verificacion(lista)
    except Exception as e:
        print("La cadena no es válida según la gramática")
        print(e)



if __name__ == '__main__':
    main()

