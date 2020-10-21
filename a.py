import os
import math

a = ['a','1','c','d'] 
b = ['1','d','2','C']
c = ['2','3','g']
d = ['3','2','4']
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

for x in range(0,len(datos)):
    for y in range(1,len(datos[x])):
        if datos[x][y] in si:
            for z in range(x,len(datos)):
                if datos[z][0] == datos[x][y]:
                    nodos[z][0] = nodos[x][y]
                    print(nodos[z][0])
                    break

print('nodos despues de cambio')
print(nodos)





               
