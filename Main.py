import os
import time

def save_text(_nombre,_autor,_editorial,_fecha):
    with open('list_books.txt','a') as save:
        # Escribimos los datos del libro en un archivo txt con los parametros que nos pasen
        save.write(f"\n\nTitulo : {_nombre}\nAutor : {_autor}\nEditorial : {_editorial}\nFecha : " + _fecha)

def load_text():
    f = open('list_books.txt','r')
    file = f.read()
    print(file)
    f.close()


class Libro():
    def __init__(self,_nombre,_autor,_editorial,_fecha):
        self.nombre = _nombre
        self.autor = _autor
        self.editorial = _editorial
        self.fecha = _fecha

#list_libros = {}

while(True):
    os.system('cls')
    print("             1. Agregar libro\n             2. Ver lista de libros\n             3. Salir")
    try:
        opc = int(input("\n        Eligue una opción : "))
        if(opc == 1):
            os.system('cls')
            nombre = input("Titulo del libro         : ")
            autor = input("Autor del libro          : ")
            editorial = input("Editorial del libro       : ")
            fecha = time.strftime("%x") #Registra la fecha
            save_text(nombre,autor,editorial,fecha)
            print("\n\n             Libro agregado!!! \n\n")
            os.system("Pause")
        elif(opc == 2):
            os.system('cls')
            print("                              Lista de libros     ")
            load_text()
            print()
            os.system("Pause")
        elif(opc == 3):
            print("\n\n                  Adios!")
            break
        else:
            print("\n           Opcion invalida\n")
            os.system("Pause")
    except:
        print("\n           Opcion invalida\n")
        os.system("Pause")
