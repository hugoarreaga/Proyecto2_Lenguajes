import threading
import time
import os


global glc  #gramatica libre del contexto 
glc = list()

global ap  #automata de pila
ap = list()


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

def opcion1_1_cargar_archivo():

    

    correcto=False
    num=0
    while(not correcto):
        

        try:
            ruta =input("direccion del archivo .glc: ")
            archivo_glc = open(ruta ,"r")
            print("     El archivo se leyo correctamente")

            correcto=True
        except :
            print('Error, introduce una direccion correcta')

    documento = archivo_glc.read()
    documento_separado = documento.split("\n%\n")

    for x in documento_separado:
        
        lineas = x.split('\n')                      # eliminar lineas vacias ↓↓↓
        for j in lineas:
            if j.isspace():
                lineas.remove(j)
            if j =='%':
                lineas.remove(j)           # eliminar lineas vacias ↑↑↑
        
        glc1 = cglc()
        glc1.producciones = []                       # limpiar atributo producciones para cada recorrido
        glc1.nombre = lineas[0]                      # objeto glc __________ nombre
        glc1.no_terminales = lineas[1].split(',')    # objeto glc __________ no terminales
        glc1.terminales = lineas[2].split(',')       # objeto glc __________ terminales
        glc1.no_terminal_i = lineas[3]               # objeto glc __________ no terminal inicial
        
        for y in range(4,len(lineas)):
            linea = lineas[y].replace(">"," ")
            alfabeto = linea.split(" ")                  # lista de cada alfabeto utilizado por linea
            glc1.producciones.append(alfabeto)       # objeto glc __________ produccion_n

        glc.append(glc1)                             # objeto glc __________ guardar objeto en lista

    ####
    imprimir_glc()
     
    
def imprimir_glc():
    for x  in glc:
        print('')
        print('NOMBRE DE LA GRAMATICA: '+x.nombre)
        print('NO TERMINALES: ')
        print(x.no_terminales)
        print('TERMINALES: ')
        print(x.terminales)
        print('NO TERMINAL INICIAL: ')
        print(x.no_terminal_i)
        print('PRODUCCIONES: ')
        for y in x.producciones:
            print(y)
        print('* _ * _ * _ * _ * _ * _ * _ * _ * _ *')
    return 0


################################################# menusss ##########################################
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
            print('     CARGAR UN NUEVO ARCHIVO DE GRAMATICAS LIBRES DE CONTEXTO')
            opcion1_1_cargar_archivo()
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

        ## opcion salir
def salir():
    print('')
    print('     *******************************')
    print('     GRACIAS POR UTILIZAR EL SISTEMA')
    print('     *******************************')

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
            salir()
            pase = False
        else :
            print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

class cglc:
    nombre = ''
    no_terminales= list()
    terminales = list()
    no_terminal_i =''
    producciones = list()


#### CONTEO INICIAL _______________________
def cuenta(): 
    for i in range(1,6): 
        os.system('cls')
        print ('')
        print ('        HUGO ALEXANDER ARREAGA CHOC')
        print ('        201701108')
        print ('        SISTEMA Spark Stack ')
        print (6-i) 
        time.sleep(0.25) 
        
x = threading.Thread(target = cuenta) 
x.start() 
x.join()
os.system('cls')
####_______________________

menu()

