# Ejercicio 4: Buscar elemento en una tupla
# Escribe una función que tome una tupla y un valor como entrada, y devuelva True si el valor está presente en la tupla y False si no lo está.

tupla = (1,2,'tres',True)

def buscarValor(valor, tupla):

    return valor in tupla

print(buscarValor('tres', tupla))