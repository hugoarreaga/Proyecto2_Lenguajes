import os
import math


a = 7
print(int(math.sqrt(a))+1)
print(math.sqrt(a))
if a%2 ==0:
    pass
else:
    print((a+1)/2)
'''
try:
    os.system("dot -Tpng a.dot -o a.png")    
    print('hecho')
except :
    print("aun no se ha cargado un archivo")
'''
a =['1','2','3','4']
b = list()
b.append(a)
for x in b:
    
    for y in x:
        espacio=''
        for z in range(len(y)):
            espacio+='*'
        print(str(len(y))+' '+ y+' {'+espacio+'}')

for x in a:
    print('dsaf')
    
    
    a = input('presione cualquier letra para mostrar el siguiente paso>')
    os.system(str(x)+'.png')