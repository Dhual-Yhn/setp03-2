# Set de problemas #4
# Problema 1.
# Profesor: Igor Caracci
# Profesor(Ayudante): Andres Caro
# Universidad de Santiago de Chile
# 10 de mayo del 2013
#
# Descripcion:
#
# Implemente la búsqueda binaria
# de forma recursiva en Python
# para localizar un elemento dentro
# de una lista.
#
#

def BinarySearch(A, valor):
    if ( len(A) == 0 ):
        return None
    elif ( len(A) == 1 ):
        if ( A[0] == valor ):
            return A[0]
        else:
            return None
    else:
       inicio = 0
       final = len(A)
       while(inicio < final):
            medio = int((inicio+final)/2)
            print ("Medio",medio," ", A[medio]," ", inicio," ", final)
            if(A[medio] > valor):
                final = medio
            elif(A[medio] == valor):
                return valor
            else:
                inicio = medio

def main():
    A = [1,7,5,3,8,9,10,11,12,13,14,15,16,20]
    x = input("Ingrese un numero a buscar \n")
    while not x.isdigit():
        print("n debe ser numero, error")
        x = input("Ingrese un  numero a buscar \n")
    valor = BinarySearch(A, int(x))
    if valor == None:
        print ("Elemento no se encuentra en lista")
    else:
        print ("Elemento encontrado")

if __name__ == "__main__":  #Si ejecuta como programa, invoca a main
    main()

