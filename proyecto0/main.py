import sys
import lexer
import parse 
# pip install pyparsing






def end():
    sys.exit()


def main ():
     
    ruta_archivo=input("Ingrese la ruta del archivo ( por ejemplo: proyecto0/documentos/ejemplo.txt): ")
    archivo= open(ruta_archivo).read().lower()

    lista = lexer.separar_texto(archivo)
    print()

    try:
        aceptado = parse.verificacion(lista)
        if (aceptado):
            print("La cadena es válida según la gramática\n")
        else:
            print("La cadena no es válida según la gramática\n")
    except Exception as e:
        print("La cadena no es válida según la gramática\n")
        print(e)




if __name__ == '__main__':
    main()

