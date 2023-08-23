import json
import os 

dataManuales={}
dataManuales['manuales']={}

with open ('manuales.json') as manuales:
    manu=json.load(manuales)
    dicMAnu=manu['manuales']
    for k,v in dicMAnu.items():
        dataManuales['manuales'][k]=dicMAnu[k]

def pyToJson():

    with open ('manuales.json','w') as miArchivo:
            json.dump(dataManuales,miArchivo,ensure_ascii=False,indent=8)

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")  

def validarInput(msg):
    while True:
        try: 
            n=input(msg)
            if n==None or n.strip()=="":
                msgError("Digite algun dato...") 
                continue
            break
        except Exception as e:
            msgError("Ha ocurrido un error ",e)
    return n

def validarEntero(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1:
                msgError('El valor debe ser mayor a 0...')
                continue
            break
        except ValueError:
            msgError('Ingrese el dato de forma numerica...')
    return n

def validarFloat(msg):
    while True:
        try:
            n=float(input(msg))
            return n
        except ValueError:
            msgError('Ingrese el dato de forma numerica...')

def listarManuales():
    os.system('clear')
    print("\n***LISTA DE MANUALES***")
    for k,v in dataManuales["manuales"].items():
        print(f"\n> Manual: {k}")
        print(f"\n- Autor: {v['author']}")
        print(f"- Paginas: {v['paginas']}")
        print("\n> Temas: ")
        cont=0
        for elem in v['temas']:
            cont+=1
            print(f"\nTema {cont}:")
            print(f"- Titulo: {elem['Titulo']}")
            print(f"- Clasificacion: {elem['Clasificación']}")
        print("\n","-"*30)

def buscarMan(msg):
    seguir=True
    while seguir:
        man=validarInput(msg)
        man=man.capitalize()
        if man in dataManuales["manuales"]:
            seguir=False
        else:
            msgError("> Este manual no se encuentra registrado.")
    return man

def verificarTemaAdicionar(man,msg):
    seguir=True
    while seguir:
        tem=validarInput(msg)
        tem=tem.capitalize()
        cont=0
        for elem in dataManuales["manuales"][man]["temas"]:
            if elem["Titulo"]==tem:
                cont+=1
        if cont>0:
            msgError("> Este tema ya se encuentra registrado")
        else:
            seguir=False
    return tem 
        
def validarClasificacion(msg):
    seguir=True
    while seguir:
        clasi=validarEntero(msg)
        if clasi<1 or clasi>3:
            msgError("> La clasificacion que digito es incorrecta.")
        else:
            seguir=False
    return clasi


def siNo(msg):
    seguir=True
    while seguir:
        x=validarEntero(msg)
        if x<1 or x>2:
            msgError("> Digite bien la opcion...") 
        else:
            seguir=False
    return x

def adicionarTemas(man):
    tem=verificarTemaAdicionar(man,"\n> Titulo del tema: ")
    clasi=validarClasificacion("> Clasificacion del tema (1=Básico/2=Intermedio/3=Avanzado): ")
    listaTemas=dataManuales["manuales"][man]["temas"]
    tema={
        "Titulo":tem,
        "Clasificación":clasi
    }
    listaTemas.append(tema)
    pyToJson()

def adicionarTema():
    os.system('clear')
    print("\n***ADICIONA UN TEMA***")
    print()
    man=buscarMan("> Manual al que quiere adicionar un tema: ")
    mas=siNo("> Desea adicionar mas de un tema al manual? (1=Si/2=No): ")
    if mas==1:
        num=validarEntero("> Cuantos temas desea adicionar?: ")
        for i in range (0,num):
            adicionarTemas(man)
    else:
        tem=verificarTemaAdicionar(man,"\n> Titulo del tema que desea adicionar: ")
        clasi=validarClasificacion("> Clasificacion del tema (1=Básico/2=Intermedio/3=Avanzado): ")
        listaTemas=dataManuales["manuales"][man]["temas"]
        tema={
        "Titulo":tem,
        "Clasificación":clasi
        }
        listaTemas.append(tema)
    pyToJson()

def verificarTemaEliminar(man,msg):
    seguir=True
    while seguir:
        tem=validarInput(msg)
        tem=tem.capitalize()
        cont=0
        for elem in dataManuales["manuales"][man]["temas"]:
            if elem["Titulo"]==tem:
                cont+=1
                seguir=False
        if cont==0:
            msgError("> Este tema no se encuentra registrado en el manual.")
            x=siNo("> Desea volverlo a intentar? (1=Si/2=No): ")
            if x==2:
                seguir=False
    return tem
            
def eliminartema():
    os.system('clear')
    print("\n***ELIMINA UN TEMA***\n")
    man=buscarMan("> Manual del que desea eliminar un tema: ")
    tema=verificarTemaEliminar(man,"> Tema a eliminar: ")
    for elem in dataManuales["manuales"][man]["temas"]:
        if elem["Titulo"]==tema:
            eliminar=dataManuales["manuales"][man]["temas"].index(elem)
            eliminado=dataManuales["manuales"][man]["temas"].pop(eliminar)
    pyToJson()

def crearManual():
    os.system('clear')
    print("\n***CREA UN MANUAL***\n")
    manual=validarInput("> Nombre del manual: ")
    manual=manual.capitalize()
    autor=validarInput("> Autor del manual: ")
    pag=validarEntero("> Cantidad de paginas: ")
    dataManuales["manuales"][manual]={
        "author": autor,
        "paginas": pag,
        "temas":[]
    }
    print("\n***AGREGA LOS TEMAS***\n")
    mas=siNo("> Desea adicionar mas de un tema al manual? (1=Si/2=No): ")
    if mas==1:
        num=validarEntero("\n> Cuantos temas desea adicionar?: ")
        for i in range (0,num):
            adicionarTemas(manual)
    else:
        tem=validarInput("\n> Titulo del tema que desea adicionar: ")
        clasi=validarClasificacion("> Clasificacion del tema (1=Básico/2=Intermedio/3=Avanzado): ")
        listaTemas=dataManuales["manuales"][manual]["temas"]
        tema={
        "Titulo":tem,
        "Clasificación":clasi
        }
        listaTemas.append(tema)
    pyToJson()


def eliminarManual():
    os.system('clear')
    print("\n***ELIMINA UN MANUAL***\n")
    man=buscarMan("> Manual que desea eliminar: ")
    del dataManuales["manuales"][man]
    pyToJson()

def listarTemas():
    os.system('clear')
    print("\n***LISTA DE TEMAS***\n")
    man=buscarMan("> Manual del que desea ver los temas: ")
    cont=0
    print(f"\n# Temas de {man}: ")
    for elem in dataManuales["manuales"][man]['temas']:
        cont+=1
        print(f"\n> Tema {cont}:")
        print(f"\n- Titulo: {elem['Titulo']}")
        print(f"- Clasificacion: {elem['Clasificación']}")

    
def modificarAutor(man):
    new= validarInput("\n> Nuevo autor: ")
    dataManuales["manuales"][man]["author"]=new
    pyToJson()

def modificarPaginas(man):
    new= validarEntero("\n> Nueva cantidad de paginas: ")
    dataManuales["manuales"][man]["paginas"]=new
    pyToJson()

def validarEleccionTema(listaTemas,msg):
    ref=len(listaTemas)
    seguir=True
    while seguir:
        x=validarEntero(msg)
        if x<1 or x>ref:
            msgError("> Elija correctamente. Por favor.")
        else:
            seguir=False
    return x
        
def modificarTitulo(tema,listaTemas):
    new=validarInput("\n> Ingrese el nuevo titulo: ")
    listaTemas[tema]["Titulo"]=new
    pyToJson()

def modificarClasificacion(tema,listaTemas):
    new=validarClasificacion("\n> Ingrese la nueva clasificacion del tema (1=Básico/2=Intermedio/3=Avanzado): ")
    listaTemas[tema]["Clasificación"]=new
    pyToJson()

def modificartodoEltema(tema,listaTemas): 
    newT=validarInput("\n> Ingrese el nuevo titulo: ")
    newC=validarClasificacion("> Ingrese la nueva clasificacion del tema (1=Básico/2=Intermedio/3=Avanzado): ")
    listaTemas[tema]["Titulo"]=newT
    listaTemas[tema]["Clasificación"]=newC
    pyToJson()


def modificarTemas(man):
    listaTemas=dataManuales["manuales"][man]['temas']
    for elem in listaTemas:
        cont+=1
        print(f"\n> Tema {cont}:")
        print(f"\n- Titulo: {elem['Titulo']}")
        print(f"- Clasificacion: {elem['Clasificación']}")

    modificar=validarEleccionTema(listaTemas,"> Ingrese el numero del tema que desea modificar: ")
    tema=modificar-1
    print("\n=> Usted desea modificar:")
    print("\n1. Titulo")
    print("2. Clasificacion")
    print("3. Todo")
    op=validarEntero("\n-> Opcion: ")
    if op==1:
        modificarTitulo(tema,listaTemas)
    if op==2:
        modificarClasificacion(tema,listaTemas)
    if op==3:
        modificartodoEltema(tema,listaTemas)


    
def modificarManual():
    os.system('clear')
    print("\n***MODIFICA UN MANUAL***\n")

    man=buscarMan("> Manual que desea modificar: ")
    print("\n***OPCIONES DE MODIFICAR***\n")
    print("=> Usted desea modificar: ")
    print("\n1. Autor.")
    print("2. Paginas.")
    print("3. Temas.")

    op=validarEntero("\n-> Opcion: ")

    if op==1:
        modificarAutor(man)
    if op==2:
        modificarPaginas(man)
    if op ==3:
        modificarTemas(man)


def encontrarDatos():
    xd=[]
    for k,v in dataManuales["manuales"].items():
        k=[0,0,0]
        bajo=0
        medio=0
        alto=0
        for elem in v['temas']:
            if elem["Clasificación"]==1:
                bajo+=1
                k[0]=bajo
            if elem["Clasificación"]==2:
                medio+=1
                k[1]=medio
            if elem["Clasificación"]==3:
                alto+=1
                k[2]=alto
        xd.append(k)
    return xd

def generarInforme():
    os.system('clear')
    listaDatos=encontrarDatos()
    listaManuales=[]
    for k,v in dataManuales["manuales"].items():
        listaManuales.append(k)
    max=len(listaManuales)
    with open ("datos.txt","w") as file:
        for i in range (0,max):
            file.write(f"\n\nManual {listaManuales[i]}: \n")
            file.write(f"\n\tTemas Básicos: {listaDatos[i][0]}")  
            file.write(f"\n\tTemas Intermedios: {listaDatos[i][1]}")
            file.write(f"\n\tTemas Avanzados: {listaDatos[i][2]}")
    print("Generado con exito!")

def menu():
     os.system('clear')
     seguir=True
     while seguir:
        print("\n***MANUALES TECNICOS***")
        print()
        print("MENU:")
        print()
        print("1. Listar manuales.")
        print("2. Adicionar un tema.")
        print("3. Eliminar un tema.")
        print("4. Crear un manual.")
        print("5. Eliminar un manual.")
        print("6. Listar temas de un manual.")
        print("7. Modificar manual.")
        print("8. Generar informe de datos.txt")
        print("9. Salir.")
        op=validarEntero("\nOpcion -> ")

        if op==1:
            listarManuales()
        if op==2:
            adicionarTema()
        if op==3:
            eliminartema()
        if op==4:
            crearManual()
        if op==5:
            eliminarManual()
        if op==6:
            listarTemas()
        if op==7:
            modificarManual()
        if op==8:
            generarInforme()
        if op==9:
            print("Gracias por utilizar el programa... Suerte!")
            seguir=False

menu()
xd=[]
for k,v in dataManuales["manuales"].items():
    k=[0,0,0]
    for elem in v['temas']:
        if elem["Clasificación"]==1:
            k[0]+1
        if elem["Clasificación"]==2:
            k[1]+1
        if elem["Clasificación"]==3:
            k[2]+1
    xd.append(k)
print(xd)