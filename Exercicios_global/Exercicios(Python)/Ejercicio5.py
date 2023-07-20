# Ejercicio 1: Suma de los elementos de una lista
# Escribe una función que tome una lista de números como entrada y devuelva la suma de todos los elementos.
 
lista =[5, 8, 9, 36, 879, 56, 5]

def sumalista(sumar):

    sumar = 0

    for i in lista:
        sumar += i

    return sumar

print (sumalista(lista))