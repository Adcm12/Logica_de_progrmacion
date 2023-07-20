# Ejercicio 7: Eliminar duplicados de una lista
# Escribe una función que tome una lista como entrada y devuelva una nueva lista que contenga los elementos únicos de la lista original, sin duplicados.

def eliminar_duplicados(lista):
    lista_sin_duplicados = []
    for elemento in lista:
        if elemento not in lista_sin_duplicados:
            lista_sin_duplicados.append(elemento)
    return lista_sin_duplicados

# Ejemplo de uso
mi_lista = [1, 2, 2, 3, 4, 4, 5]
lista_sin_duplicados = eliminar_duplicados(mi_lista)
print("Lista original:", mi_lista)
print("Lista sin duplicados:", lista_sin_duplicados)
