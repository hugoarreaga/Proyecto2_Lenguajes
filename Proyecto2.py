import threading
import time


def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introduce un numero entero: "))
            correcto=True
        except ValueError:
            print('     Error, introduce un numero entero')
     
    return num












################################################# menusss
def submenu1():
    pase = True
    while pase:
        print('     _____________________________________')
        print('      MENU gramáticas libres del contexto')
        print('      Seleccione una opcion')
        print('      1) Opcion 1')
        print('      2) Opcion 2')
        print('      3) Salir')
        print('     _______________________')
        opcion = pedirNumeroEntero()
        if opcion ==1:
            print('         seleciono la opcion 1')
        elif opcion ==2:
            print('         seleccion la opcion 2')
        elif opcion ==3:
            print('         seleccion la opcion 3')
            pase = False
        else :
            print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

def submenu2():
    pase = True
    while pase:
        print('     _________________________')
        print('      MENU autómatas de pila')
        print('      Seleccione una opcion')
        print('      1) Opcion 1')
        print('      2) Opcion 2')
        print('      3) Salir')
        print('     _________________________')
        opcion = pedirNumeroEntero()
        if opcion ==1:
            print('         seleciono la opcion 1')
        elif opcion ==2:
            print('         seleccion la opcion 2')
        elif opcion ==3:
            print('         seleccion la opcion 3')
            pase = False
        else:
            print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

def menu():
    pase = True
    while pase:
        print('     _________________________')
        print('      MENU INCIAL Spark Stack')
        print('      Seleccione una opcion')
        print('      1) gramáticas libres del contexto')
        print('      2) autómatas de pila')
        print('      3) Salir')
        print('     _________________________')
        opcion = pedirNumeroEntero()
        if opcion ==1:
            print('         seleciono la opcion 1')
            submenu1()
        elif opcion ==2:
            print('         seleccion la opcion 2')
            submenu2()
        elif opcion ==3:
            print('         seleccion la opcion 3')
            pase = False
        else :
            print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0
        
def cuenta(): 
    for i in range(1,6): 
        print (6-i) 
        time.sleep(1) 
        
x = threading.Thread(target = cuenta) 
x.start() 
x.join()

menu()

