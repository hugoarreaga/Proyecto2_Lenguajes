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
########################### OPCIONES DE AUTOMATAS DE PILA     ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓######################

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
    ################################ opcion extra 
def crear_pdf_ap(x):
    file = open(x.nombre+'.dot', "w")
    file. write("digraph G {" + os.linesep) # primera linea
    ### nodos
    file. write('    rankdir =LR ; ' + os.linesep)   # estilo de relaciones
            ###### tabla de datos

    
    file.write(' Nodo_Tablero [shape=none, margin=0 ,label=< '+ os.linesep)
    file.write('<TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">'+ os.linesep)
    file.write('<TR><TD align="left"> Nombre = <b>'+x.nombre+'</b></TD></TR>'+ os.linesep)
    texto =''
    for y in range(0,len(x.alfabeto)):
        if y == 0:  texto += x.alfabeto[y]
        else:       texto += ','+x.alfabeto[y]
    file.write('<TR><TD align="left"> Alfabeto: { '+texto+' }</TD></TR>'+ os.linesep)
    
    texto =''
    for y in range(0,len(x.simbolo_pila)):
        if y == 0:  texto += x.simbolo_pila[y]
        else:       texto += ','+x.simbolo_pila[y]
    file.write('<TR><TD align="left"> Alfabeto de pila: { '+texto+' }</TD></TR>'+ os.linesep)

    texto =''
    for y in range(0,len(x.estados)):
        if y == 0:  texto += x.estados[y]
        else:       texto += ','+x.estados[y]
    file.write('<TR><TD align="left"> Estados: { '+texto+' }</TD></TR>'+ os.linesep)


    file.write('<TR><TD align="left"> Estado inicial: { '+x.estados_i+' }</TD></TR>'+ os.linesep)
    file.write('<TR><TD align="left"> Estado de aceptacion: { '+x.estados_a+' }</TD></TR>'+ os.linesep)
    file.write('</TABLE>>];'+ os.linesep)
        #######################
    file.write('Nodo_Vacio [shape=none, label=""]')
    file.write('Nodo_Vacio -> '+x.estados_i + os.linesep)
    file.write('Nodo_Tablero -> Nodo_Vacio [color = white]'+ os.linesep)
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

    print('\n           EL ARCHIVO .PNG DEL AUTOMATA "'+x.nombre+'" LOGRO GENERARSE CORRECTAMENTE\n')
    os.system('dot -Tpng '+x.nombre+'.dot -o '+x.nombre+'.png')    
    os.system(x.nombre+'.png')

    return 0


def opcion2_3_validar_cadena():
    nombre = obtener_ap_especifico()
    dato = []
    for x in ap:
        if x.nombre == nombre:
            dato = validar_cadena_2_3(x)    
            if dato[0] == True :
                print('\n    ************  LA CADENA ES VALIDA  ************\n')
            else:
                print('\n    ************  CADENA ES INVALIDA   ************\n')
    return 0


def validar_cadena_2_3(x):
    cadena = input ('Ingrese la cadena a validar: ')
    ##cadena = '#'+cadena1+'#'
    listaletras = list(cadena)
    camino = []
    pila = []
    estadopila=[]
    letraserrores=[]
    estadoentrada =['']

    origen = x.estados_i 
    
    for y in x.trancisiones:
        if y[0] == origen:
            s = '-'.join([str(elem) for elem in pila])
            estadopila.append(s)
            camino.append(y)
            origen = y[3]
            if y[4] != '$':
                pila.append(y[4])
            if y[2] != '$':
                del pila[-1]
                ## inserta
            break     

    estavaciab = False   

    estavacia = False
    existeletra =False

    sacandoinexistente = False
    errorinexistente = False

    sacaincorrecto = False
    estadoactual = ''
    for y in listaletras:
        existeletra =False
        
        for z in x.trancisiones:
            if origen == z[0] and z[1] == y :
                existeletra = True
                if z[2] == pila[-1] or z[2]=='$':
                    s = ''.join([str(elem) for elem in pila])
                    estadoactual = estadoactual +y 
                    estadopila.insert(0,s)
                    estadoentrada.append(estadoactual)
                    camino.append(z)
                    ## extrae
                    if z[2] != '$':
                        aa = ['#']
                        if pila == aa:
                            estavacia = True
                        if pila[-1] == z[2]:
                            try:
                                pila.pop()
                            except :
                                estavacia = True
                                print('sacando de mas')
                            '''if len(pila) ==0:
                                estavacia = True
                                
                            else:
                                del pila[-1]'''
                        else:
                            sacaincorrecto = True
                    ## inserta
                    if z[4] != '$':
                        pila.append(z[4])
                    origen = z[3]
                    break
                else:
                    estavacia = True
        if existeletra ==False:
            letraserrores.append(y)
    
    estadoentrada.append(estadoactual)
    estadoentrada.append(estadoactual)

    for y in x.trancisiones:
        sacaincorrecto = False
        if y[3] == x.estados_a and origen ==y[0]:
            s = '-'.join([str(elem) for elem in pila])
            estadopila.insert(0,s)
            camino.append(y)
            if y[2] != '$':
                if pila[-1] == y[2]:
                    try:
                        pila.pop()
                    except :
                        estavacia = True
                    #if not len(pila):
                    #    estavacia = True
                    #else:
                    #    del pila[-1]
                else:
                    sacaincorrecto = True
                ## inserta
            if y[4] != '$':
                pila.append(y[4])
            s = '-'.join([str(elem) for elem in pila])
            estadopila.insert(0,s)
            break
    
    
    
    cadena_valida = False
    if not pila and estavacia == False:
        cadena_valida = True
    else:
        cadena_valida = False
    
    '''
    cadena_valida = False
    if len(pila) ==0 and estavacia == False and sacandoinexistente==True :
        cadena = True
    '''
    if len(letraserrores)==0:
        pass
    else:
        print('Estas letras no forman parde de los terminales')
        for y in letraserrores:
            print(y)
    
    return [cadena_valida, camino,estadoentrada,estadopila, x.nombre]

def opcion2_4_ruta_validacion():
    nombre = obtener_ap_especifico()
    dato = []
    for x in ap:
        if x.nombre == nombre:
            dato = validar_cadena_2_3(x)    
            if dato[0] is True :
                print('\n    ************  LA CADENA ES VALIDA  ************\n')
            else:
                print('\n    ************  CADENA ES INVALIDA   ************\n')
    
    if dato[0] is True:
        print('\nRuta:')
        for x in dato[1]:
            print(x[0]+','+x[1]+','+x[2]+';'+x[3]+','+x[4])
    return 0

def opcion2_6_validar_cadena_pasada():

    nombre = obtener_ap_especifico()
    dato = []
    for x in ap:
        if x.nombre == nombre:
            dato = validar_cadena_2_3(x)    
            if dato[0] is True :
                print('\n    ************  LA CADENA ES VALIDA  ************\n')
            else:
                print('\n    ************  CADENA ES INVALIDA   ************\n')
    
    estadopila =[]
    camino = []
    estadoentrada = []
    if dato[0] is True:
        camino = dato[1]
        estadoentrada = dato[2]
        estadopila = dato[3]
        nombre = dato[4]
        caminoordenado = []
        for x in camino:
            linea = ''
            linea = x[0]+','+x[1]+','+x[2]+';'+x[3]+','+x[4]
            caminoordenado.append(linea)
        caminoordenado.append(' ')


        file = open(nombre+'-pasada.dot', "w")
        file. write("digraph G {" + os.linesep) # primera linea
        file.write('    Nodo_Tablero [shape=none, margin=0 ,label=< '+ os.linesep)
        file.write('    <TABLE BORDER="1" CELLBORDER="1" CELLSPACING="0">'+ os.linesep)
        file.write('    <TR>  <TD align="left"> ITERACION </TD> <TD align="left"> PILA </TD><TD align="left"> ENTRADA </TD><TD align="left"> TRANSICION </TD> </TR>'+ os.linesep)
        iteracion = 0
        for x in range(0, len(caminoordenado)):
            file.write('    <TR>  <TD align="left"> '+str(iteracion)+' </TD> <TD align="left"> '+str(estadopila[x])+' </TD><TD align="left"> '+str(estadoentrada[x])+' </TD><TD align="left"> '+str(caminoordenado[x])+' </TD> </TR>'+ os.linesep)
            iteracion = iteracion+1

        file.write('</TABLE>>];'+ os.linesep)
        file.write('}')
        file.close()

        os.system('dot -Tpdf '+nombre+'-pasada.dot -o '+nombre+'-pasada.pdf')    
        os.system(nombre+'-pasada.pdf')
        
    return 0

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

    return 0

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

#def opcion1.2_mostrar_informacion()        

def opcion1_2_mostrar_informacion():
    nombre = obtener_glc_especifico()
    for y in glc:
        if y.nombre == nombre:
            imprimir_1_2(y)
    nombre = 'no_existe'
            
    return 0

def imprimir_1_2(y):
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

    producc = []
    for x in y.producciones:
        for z in range(1,len(x)):
            lin = []
            lin.append(x[0])
            lin.append(x[z])
            producc.append(lin)
    producc.sort()
    espacionombre=''
    actual = producc[0][0]
    print(producc[0][0]+' > '+producc[0][1])
    for x in range(1,len(producc)):
        
        espacionombre=''
        for z in range(len(producc[x][0])): espacionombre+=' '
        
        if producc[x][0] == actual:  print(espacionombre+' | '+producc[x][1])
        else: 
            actual = producc[x][0]
            print(producc[x][0]+' > '+producc[x][1])     
     

    print('   *-*-*-*-*-*-*-*-*-*-*-*\n')
    continuar = input('Presione "Enter" para continuar')
    os.system('cls')
    return 0 

def opcion1_3_generar_arbol():
    nombre = obtener_glc_especifico()
    for x in glc:
        if nombre == x.nombre:
            generar_arbol_pdf(x)

    return 0

def generar_arbol_pdf(x):
    file = open(x.nombre+'-arbol.dot', "w")
    file. write("graph G {" + os.linesep) # primera linea
    ### crear lista de nodos
    nodos = []
    
    ac = 100
    for i in range(0,len(x.producciones)):
        linea= [] 
        for y in range(0,len(x.producciones[i])):
            linea.append(ac)
            ac = ac+1
        nodos.append(linea)
    #### crear lista de nodos
    print(nodos)
    print(x.producciones)
    ### cambiar nodos
    for i in range(0,len(x.producciones)):
        for y in range(1,len(x.producciones[i])):
            if x.producciones[i][y] in x.no_terminales:
                for z in range(i+1,len(x.producciones)):
                    if x.producciones[z][0] == x.producciones[i][y]:
                        nodos[z][0] = nodos[i][y]
                        break
    print(nodos)

    ### cambiar nodos
    for i in range(0,len(nodos)):
        for j in range(0,len(nodos[i])):
            file.write(str(nodos[i][j]) + '  [ label = '+str(x.producciones[i][j])+ ' ,shape = none ]'+os.linesep)
    
    file.write(str(x.nombre)+' [shape = box]' + os.linesep )
    file.write(str(x.nombre)+' -- 100 [color = white];' + os.linesep )

    for i in range(0,len(nodos)):
        for j in range(1,len(nodos[i])):
            file.write(str(nodos[i][0])+' -- '+str(nodos[i][j]) +' ;'+os.linesep)

    file.write('}')
    file.close()
    
    print('\n           EL ARCHIVO .PNG DEL ARBOL DE DERIVACION "'+x.nombre+'" LOGRO GENERARSE CORRECTAMENTE\n')
    os.system('dot -Tpng '+x.nombre+'-arbol.dot -o '+x.nombre+'-arbol.png')
    return 0
    
def opcion1_4_generar_automata():
    nombre = obtener_glc_especifico()
    for x in glc:
        if nombre == x.nombre:
            generar_automata_equivalente_pdf(x)

    return 0

def generar_automata_equivalente_pdf(x):
    file = open(x.nombre+'auto_equiv.dot', "w")
    file. write("digraph G {" + os.linesep) # primera linea
    ### nodos
    file. write('    rankdir =TD ;\n    splines=line;\n    tailclip=false ;' + os.linesep)   # estilo de relaciones

    ###### nodo extra ----- tabla de datos

    file.write('        /* Entities */ '+ os.linesep)
    file.write('    Nodo_Tablero [shape=none, margin=0 ,label=< '+ os.linesep)
    file.write('    <TABLE BORDER="1" CELLBORDER="0" CELLSPACING="0">'+ os.linesep)
    file.write('    <TR><TD align="left"> Nombre = <b>'+x.nombre+'</b></TD></TR>'+ os.linesep)
    texto =''
    for y in range(0,len(x.terminales)):
        if y == 0:  texto += x.terminales[y]
        else:       texto += ','+x.terminales[y]
    file.write('    <TR><TD align="left"> Alfabeto: { '+texto+' }</TD></TR>'+ os.linesep)
    
    for y in x.no_terminales:
        texto += ','+str(y)
    texto +=',#'
    file.write('    <TR><TD align="left"> Alfabeto de pila: { '+texto+' }</TD></TR>'+ os.linesep)

    file.write('    <TR><TD align="left"> Estados: { i,q,p,f }</TD></TR>'+ os.linesep)
    file.write('    <TR><TD align="left"> Estado inicial: { i }</TD></TR>'+ os.linesep)
    file.write('    <TR><TD align="left"> Estado de aceptacion: { f }</TD></TR>'+ os.linesep)
    file.write('    </TABLE>>];'+ os.linesep)

    #############

    #### nodos medios
    
    file.write('    i [shape = circle , style = filled , color = lightblue                   ] ; '+ os.linesep)
    file.write('    p [shape = circle , style = filled , color = lightblue                   ] ; '+ os.linesep)
    file.write('    q [shape = circle , style = filled , color = lightblue , margin = 1      ] ; '+ os.linesep)
    file.write('    f [shape = circle , style = filled , color = lightblue , peripheries = 3 ] ; '+ os.linesep)             
    #### nodos separadores
    file.write('    arriba [shape=none,label=""] ; '+ os.linesep)
    file.write('    vacio  [shape=none,label=""] ; '+ os.linesep)
    file.write('    abajo  [shape=none,label=""] ; '+ os.linesep)


    #### nodos arriba --- terminales
    producciones = 100
    for y in x.producciones:
        nodoparcial=''
        for z in range(1,len(y)):
            nodoparcial+=y[z]
        nodo = '$,'+str(y[0])+';'+nodoparcial
        
        file.write('    '+str(producciones)+' [ shape = plaintext , label = "'+nodo+'" ] ; '+ os.linesep)
        producciones = producciones+1

    #### nodos abajo --- producciones
    terminales = 200
    for y in x.terminales:
        nodo = str(y)+','+str(y)+';$'
        file.write('    '+str(terminales)   +' [ shape = plaintext , label = "'+nodo+'" ] ; '+ os.linesep)
        terminales = terminales+1
    
    #######################################         /* Relationships */

    file.write('        /* Relationships */' +os.linesep)
    file.write('    Nodo_Tablero -> arriba -> vacio -> abajo  [ color = white ] ; '+os.linesep)

    #____# relaciones linea arriba con producciones invisible
    aa=''
    producciones=100
    for y in x.producciones:
        aa += ' -> '+ str(producciones)
        producciones = producciones+1
    file.write('    arriba '+aa+' [ color = white ] ;'+os.linesep)

    #____# relaciones linea medio invibles
    
    file.write('    vacio -> i ;'+ os.linesep)
    file.write('    vacio -> i -> p -> q -> f [ color = white ] ; '+os.linesep)

    #____# relaciones linea medio visibles
    file.write('    i -> p [ label = "$,$;#" ] ;'+ os.linesep)
    file.write('    p -> q [ label = "$,$;'+x.no_terminal_i+'" ] ;'+ os.linesep)
    file.write('    q -> f [ label = "$,#;$" ] ;'+ os.linesep)

    #____# relaciones linea abajo con terminales invisible
    aa=''
    terminales = 200
    for y in x.terminales:
        aa += " -> "+ str(terminales)
        terminales = terminales+1
    file.write('    abajo '+aa+' [ color = white ] ;'+os.linesep)

    
    
    #____# relaciones producciones
    producciones = 100
    for y in x.producciones:
        file.write('    '+str(producciones)+' -> q ; q -> '+str(producciones)+' [ dir = none] ;'+ os.linesep)
        producciones = producciones+1

    #____# relaciones terminales
    terminales = 200
    for y in x.terminales:
        file.write('    '+str(terminales)  +' -> q ; q -> '+str(terminales)  +' [ dir = none] ;'+ os.linesep)
        terminales = terminales +1




    #############################################           ranks
    file.write('        /* Ranks */'+os.linesep)

    
    #____# rank de las producciones arriba
    rankproducciones=''
    producciones = 100
    for y in x.producciones:
        rankproducciones += ' ; '+str(producciones)
        producciones = producciones+1
    file.write('    { rank = same ; arriba'+rankproducciones +'} ;'+os.linesep)

        
    #____# rank de los medios
    file.write('    { rank = same ; vacio ; i ; p ; q ; f } ;'+os.linesep)

    
    #____# rank terminales abajo
    rankterminales=''
    terminales = 200
    for y in x.terminales:
        rankterminales +=' ; '+ str(terminales)
        terminales = terminales+1
    file.write('    { rank = same ; abajo'+rankterminales   +'} ;'+os.linesep)

        

    file. write("}"+ os.linesep)  # ultima linea
    file. close()

    print('\n           EL ARCHIVO .PDF DEL AUTOMATA EQUIVALENTE "'+x.nombre+'" LOGRO GENERARSE CORRECTAMENTE\n')
    os.system('dot -Tpdf '+x.nombre+'auto_equiv.dot -o '+x.nombre+'auto_equiv.pdf')    
    ##os.system(x.nombre+'.pdf')

    return 0

####################################################################################################
####################################################################################################
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
            opcion1_3_generar_arbol()
        elif opcion ==4:
            print('     GENERAR AUTOMATA DE PILA EQUIVALENTE')
            opcion1_4_generar_automata()
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
        elif opcion ==3:
            print('         VALIDAR UNA CADENA')
            opcion2_3_validar_cadena()
        elif opcion ==4:
            print('         RUTA DE VALIDACION')
            opcion2_4_ruta_validacion()
        elif opcion ==5:
            print('         RECORRIDO PASO A PASO')
        elif opcion ==6:
            print('         VALIDAR CADENA EN UNA PASADA')
            opcion2_6_validar_cadena_pasada()
        elif opcion ==7:
            print('         seleccionp la opcion 7')
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

