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



############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
########################### OPCIONES DE AUTOMATAS DE PILA     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓

def opcion2_1_cargar_archivo():
    correcto=False
    num=0
    while(not correcto):
        

        try:
            ruta =input("direccion del archivo .ap: ")
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
                lineas.remove(j)                    # eliminar lineas vacias ↑↑↑
        
        ap1 = cap()
        ap1.trancisiones = []                       # limpiar atributo producciones para cada recorrido

        ap1.nombre = lineas[0]                      # objeto ap __________ nombre
        ap1.alfabeto = lineas[1].split(',')         # objeto ap __________ alfabeto
        ap1.simbolo_pila = lineas[2].split(',')     # objeto ap __________ simbolos de pila
        ap1.estados = lineas[3].split(',')          # objeto ap __________ estados
        ap1.estados_i = lineas[4]                   # objeto ap __________ estado inicial
        ap1.estados_a = lineas[5]                   # objeto ap __________ estado aceptacion
        
        for y in range(6,len(lineas)):
            linea = lineas[y].replace(";",",")
            alfabeto = linea.split(",")              # lista de cada elemento utilizado en la transicion
            ap1.trancisiones.append(alfabeto)       # objeto glc __________ produccion_n
        unico= True
        for x in ap:
            if ap1.nombre == x.nombre:
                print('     ****ya se agrego un automata de pila con ese nombre')
                unico=False
        if unico:
              
            ap.append(ap1)                             # objeto glc __________ guardar objeto en lista
    si = input('    Presione "y" si desea imprimir los datos guardados o cualquier letra para continuar:')
    if si =='y':    imprimir_ap()

### opcion extra    
def imprimir_ap():
    for x in ap:

        print('')
        print('NOMBRE DEL AUTOMATA: '+x.nombre)
        print('ALFABETOS: ')
        print(x.alfabeto)
        print('SIMBOLOS DE PILA: ')
        print(x.simbolo_pila)
        print('ESTADOS: ')
        print(x.estados)
        print('ESTADO INICIAL: ')
        print(x.estados_i)
        print('ESTADO ACEPTACION: ')
        print(x.estados_a)
        for y in x.trancisiones:
            print(y)
        print('\n* _ * _ * _ * _ * _ * _ * _ * _ * _ *')
    return 0

def obtener_ap_especifico():
    paso = True
    if not ap:
        print('aun no a cargado ningun ap ')
        return 'no_existe'
    else:
        while paso:
            print('\n   Listado de automatas guardadas:')
            for x in ap:
                print(' -/-> '+x.nombre)
            nombre = input('    A continuacion escriba el nombre del automata que desea elegir:  ')
            for x in ap:
                if nombre == x.nombre:
                    paso= False
                    return x.nombre
            print('El automata no existe, intente con un nuevo nombre')

def opcion2_2_mostrar_informacion():
    nombre = obtener_ap_especifico()
    for x in ap:
        if x.nombre == nombre:
            crear_pdf_ap(x)

    return 0
#### opcion extra 
def crear_pdf_ap(x):
    file = open(x.nombre+'.dot', "w")
    file. write("digraph G {" + os.linesep) # primera linea
    ### nodos
    file. write("    rankdir =LR ;" + os.linesep)   # estilo de relaciones
    for y in x.estados:
        if y == x.estados_a:    
            file. write('    '+y +'[shape= doublecircle]'+ os.linesep)            # nodos final
        else:
            file. write('    '+y +'[shape= circle]'+ os.linesep)                  # nodos
    
    for y in x.trancisiones:
        mensaje = y[1]+','+y[2]+';'+y[4]
        file.write('    '+y[0] +'->'+y[3]+'[label ="'+mensaje+'"]'+os.linesep)



    file. write("}"+ os.linesep)  # ultima linea
    file. close()

    print('\n           EL ARCHIVO .PNG DEL AUTOMATA '+x.nombre+' LOGRO GENERARSE CORRECTAMENTE\n')
    os.system('dot -Tpng '+x.nombre+'.dot -o '+x.nombre+'.png')    
    os.system(x.nombre+'.png')

    return 0

############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
########################### OPCIONES DE GRAMATICAS REGULARES LIBRES DE CONTEXTO     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓



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
                lineas.remove(j)                    # eliminar lineas vacias ↑↑↑
        
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
        unico= True
        for z in glc:
            if glc1.nombre == z.nombre:
                print('     ****ya se agrego una gramatica libre de contexto con ese nombre')
                unico=False
        term = False
        
        for aa in glc1.producciones:
            noter = 0
            for bb in range(2,len(aa)):
                if str(aa[bb]) in glc1.terminales:      term =True
            for bb in range(1,len(aa)):
                if str(aa[bb]) in glc1.no_terminales:   noter+= 1
            if noter >1:    term=True
        if term==False:print('      *****La gramatica con nombre: "'+glc1.nombre+'" no es libre de contexto')
        if unico and term:  glc.append(glc1)                             # objeto glc __________ guardar objeto en lista

    ####
    si = input('    Presione "y" si desea imprimir los datos guardados o cualquier letra para continuar:')
    if si =='y':    imprimir_glc()
     
### opcion extra    
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
        print('\n* _ * _ * _ * _ * _ * _ * _ * _ * _ *')
    return 0

### opcion extra    
def obtener_glc_especifico():
    paso = True
    if not glc:
        print('aun no a cargado ningun glc ')
        return 'no_existe'
    else:
        while paso:
            print('\n   Listado de gramaticas libres de contexto guardadas:')
            for x in glc:
                print(' -/-> '+x.nombre)
            nombre = input('    A continuacion escriba el nombre de la gramatica que desea elegir:  ')
            for x in glc:
                if nombre == x.nombre:
                    paso= False
                    return x.nombre
                else:
                    print('La gramatica no existe, intente con un nuevo nombre')

#def opcion1_2_mostrar_informacion()        

def opcion1_2_mostrar_informacion():
    nombre = obtener_glc_especifico()
    for y in glc:
        if y.nombre == nombre:
            print('\n   *-*-*-*-*-*-*-*-*-*-*-*')
            print('   INFORMACION DEL AUTOMATA SELECCIONADO')
            print('     Nombre:         {'+y.nombre+'}')
            noterminales =''
            for x in range(0,len(y.no_terminales)):
                if x==0: noterminales += y.no_terminales[x]
                else: noterminales += ', '+y.no_terminales[x]
            print('     No Terminales:  {'+noterminales+'}')
            terminalles=''
            for x in range(0,len(y.terminales)):
                if x==0: terminalles+= y.terminales[x]
                else: terminalles += ', '+y.terminales[x]
            print('     Terminales:     {'+terminalles+'}')
            print('     No Terminal Ini:{'+y.no_terminal_i+'}')
            print('     Producciones:')
            for x in y.producciones:
                produccionn=''
                espacionombre=''
                for z in range(len(x[0])): espacionombre+=' '
                for y in range(1,len(x)):
                    if y ==1: print('                     { '+x[0]+' > '+x[y] +' }')
                    else:print('                     { '+espacionombre+' | '+x[y] +' }')
            print('   *-*-*-*-*-*-*-*-*-*-*-*\n')
    return 0


def opcion1_3_generar_arbol():
    y = obtener_glc_especifico()
    if y is none:
        print('Aun no se ha cargado ningun archivo')
    else:
        file = open("imagen.dot", "w")
        file.write("graph G {" + os.linesep) # primera linea
        file.write("rankdir =TD ;splines=line; tailclip=true" + os.linesep) 
        lista_nodos=list()
        for x in y.producciones:
            for z in x:
                if z in lista_nodos:
                    pass
                else:
                    lista_nodos
        file.write()
        file.close()

##################################################################################################
###################################################################################################
###################################################################################################
###################################################################################################    
##################################################################################################
################################################# menusss ##########################################


def submenu1():
    pase = True
    while pase:
        print('     _____________________________________')
        print('      MENU gramáticas libres del contexto')
        print('      Introduce el numero asociado a la izquierda de la opcion deseada')
        print('       1)     Cargar un nuevo archivo de gramaticas libres de contexto')
        print('       2)     Mostrar informacion general')
        print('       3)     Arbol de Derivación')
        print('       4)     Generar automata de pila equivalente')
        print('       5)     Salir')
        print('     _______________________')
        opcion = pedirNumeroEntero()
        if   opcion ==1:
            print('     CARGAR UN NUEVO ARCHIVO DE GRAMATICAS LIBRES DE CONTEXTO')
            opcion1_1_cargar_archivo()
        elif opcion ==2:
            print('     MOSTRAR INFORMACION GENERAL')
            opcion1_2_mostrar_informacion()
        elif opcion ==3:
            print('     ARBOL DE DERIVACION')
            pase = False
        elif opcion ==4:
            print('     GENERAR AUTOMATA DE PILA EQUIVALENTE')
        elif opcion ==5:
            print('     Salió del menu "gramaticas libre de contexto" ')
            pase = False
        else :
            print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

def submenu2():
    pase = True
    while pase:
        print('     _________________________')
        print('      MENU autómatas de pila')
        print('      Introduce el numero asociado a la izquierda de la opcion deseada')
        print('       1)    Cargar archivo de automata de pila')
        print('       2)    Mostrar información de autómata')
        print('       3)    Validar una cadena')
        print('       4)    Ruta de validacion')
        print('       5)    Recorrido paso a paso')
        print('       6)    Validar cadena en una pasada')
        print('       7)    Salir')
        
        print('     _________________________')
        opcion = pedirNumeroEntero()
        if   opcion ==1:
            print('         CARGAR ARCHIVO DE AUTOMATA DE PILA')
            opcion2_1_cargar_archivo()
        elif opcion ==2:
            print('         MOSTRAR INFORMACION DEL AUTOMATA')
            opcion2_2_mostrar_informacion()
        elif opcion ==3:print('         seleccion la opcion 2')
        elif opcion ==4:print('         seleccion la opcion 3')
        elif opcion ==5:print('         seleccion la opcion 2')
        elif opcion ==6:print('         seleccion la opcion 3')
        elif opcion ==7:
            print('         seleccion la opcion 3')
            pase = False
        else:           print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

        ## opcion salir
def salir():
    yy = threading.Thread(target= cuenta_salir)
    yy.start()
    yy.join()

def menu():
    pase = True
    while pase:
        print('     _________________________\n      MENU INCIAL Spark Stack\n      Introduce el numero asociado a la izquierda de la opcion deseada')
        print('       1)    gramáticas libres del contexto\n       2)    autómatas de pila\n       3)    Salir\n     _________________________')
        opcion = pedirNumeroEntero()
        if   opcion ==1:
            print('         seleciono la opcion 1')
            submenu1()
        elif opcion ==2:
            print('         seleccion la opcion 2')
            submenu2()
        elif opcion ==3:    
            salir()
            pase = False
        else:           print('     **DEBE ELEGIR UNA DE LAS OPCIONES DISPONIBLES**')
    return 0

class cglc:
    nombre = ''
    no_terminales= list()
    terminales = list()
    no_terminal_i =''
    producciones = list()

class cap:
    nombre = ''
    alfabeto= list()
    simbolo_pila = list()
    estados= list()
    estados_i =''
    estados_a =''
    trancisiones = list()

#### CONTEO INICIAL _______________________
def cuenta(): 
    for i in range(1,6): 
        os.system('cls')
        print ('')
        print ('        HUGO ALEXANDER ARREAGA CHOC')
        print ('        201701108')
        print ('        SISTEMA Spark Stack ')
        print ('               '+str(6-i)) 
        time.sleep(0.25) 
#### CONTEO FINAL
def cuenta_salir():
    
    for i in range(1,6):
        os.system('cls')
        print('\n     *******************************\n     GRACIAS POR UTILIZAR EL SISTEMA')
        print('                     '+str(6-i))
        print('                  ADIOSSS\n     *******************************')
        time.sleep(0.75) 
    os.system('cls')

x = threading.Thread(target = cuenta) 
x.start() 
x.join()
os.system('cls')
####_______________________

menu()

