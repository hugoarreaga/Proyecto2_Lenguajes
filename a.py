import os
import math

a = ['a','1','c','d'] 
b = ['c','d','2','C']
c = ['2','3','g']
d = ['b','2','4']
e = ['2','e','3']
f = ['3','w','z']

datos = list()
datos.append(a)
datos.append(b)
datos.append(c)
datos.append(d)
datos.append(e)
datos.append(f)
print (datos)
nodos = []
ac = 100
for x in range(0,len(datos)):
    linea= [] 
    for y in range(0,len(datos[x])):
        linea.append(ac)
        ac = ac+1
    nodos.append(linea)
print(nodos)
si =['1','2','3']
print(si)

for i in range(0,len(datos)):
    for y in range(1,len(datos[i])):
        if datos[i][y] in si:
            for z in range(i,len(datos)):
                if datos[z][0] == datos[i][y]:
                    nodos[z][0] = nodos[i][y]
                    print(nodos[z][0])
                    break

print('nodos despues de cambio')
print(nodos)

susu= []
susu.append('S>A a B')
susu.append('A>a A')
susu.append('A>a')
susu.append('B>b C a')
susu.append('C>c')
susu.sort()
datos.sort()
print(datos)


               
