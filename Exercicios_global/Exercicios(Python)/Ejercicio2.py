# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

import math

numero = int(input('Informe un numero: '))

doble = numero **2
raiz = math.sqrt(numero)

print(f'''El doble del numero informado es {doble} y su raiz cuadrada es {round(raiz, 2)}''')


