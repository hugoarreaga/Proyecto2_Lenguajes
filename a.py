import os
import math



cadena = '1234'

lista = list(cadena)
print(lista)
print('"'+lista[-1]+'"')


lista.pop()
lista.pop()
lista.pop()
lista.pop()
try:
    lista.pop()
except :
    print('sacando de una lista')

for x in range(0,len(lista)):
    print(lista[x])
               
bb = []
print(len(bb))