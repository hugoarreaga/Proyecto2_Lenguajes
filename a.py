import os
import math



cadena = 'Ingrese la cadena a validar: '

lista = list(cadena)
print(lista)
print('"'+lista[-1]+'"')
a = len(lista) -1
for x in range(0,len(lista)):
    print(lista[a-x])
               
print('aa')