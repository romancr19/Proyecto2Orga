import json

# Aca se almacena en una variable lo contenido en el json

def cargarDelJson():
    with open("pinturas.json", "r") as f:
        jsonString = f.read()
        return json.loads(jsonString)

#Se pone la 1era letra mayuscula de cada nombre de las pinturas    

def nombresCapitalizados():
    global listaPinturas
    listaPinturas = cargarDelJson()
    for i in listaPinturas:
        for j in i['Nombre']:
            j.capitalize()
    return listaPinturas


def indexCotas():
    indiceCotas = {}
    indiceCotasOrdenado = {}
    cotas = []
    contador = 0
    
    for i in listaPinturas:
        cotas.append(i['Cota'])
        indiceCotas[i['Cota']] = contador
        contador += 1
       
    cotas.sort()    

    for i in cotas:
        for j in indiceCotas:
            if i == j:
                indiceCotasOrdenado[i] = indiceCotas[j]
                break

    tuplaCotas = indiceCotasOrdenado.items()
    listaCotas = []
    for i in tuplaCotas:
        listaCotas.append(list(i))

#Se retorna un diccionario de cotas ordenados alfabeticamente con su posicion en el vector principal 
#y en forma de lista    

    return indiceCotasOrdenado, listaCotas
    

#Se pide que el usuario ingrese un cota
def elementoIngresado():
    elemento = input('Ingrese la cota que desea buscar: ')
    elemento = elemento.upper()
    return elemento

#Se busca el elemento por busqueda binaria
def busquedaBinariaCotas(lista,elemento):   
    x = len(lista)
    y = x//2
    z = lista[y][0] 
    if z == elemento:
        print('Encontrado')
        indice = lista[y][1]
        
        print(f'''A continuacion, los datos de la pintura con cota "{elemento}":
{listaPinturas[indice]}''')
    elif z != elemento and len(lista) <= 1:
        print('No esta lo que pusiste')   
    elif len(lista) == 2 and z != elemento:
        lista2 = lista[0:1]
        busquedaBinariaCotas(lista2,elemento)  #tupla2,elemento
    elif elemento > z:
        lista2 = lista[y:x+1]
        busquedaBinariaCotas(lista2,elemento)  
    elif elemento < z:
        lista2 = lista[0:y+1]
        busquedaBinariaCotas(lista2,elemento)  
    else:
        pass


#Se crea una funcion para las cotas que se usara en el archivo del menu

def coticas():
    b = indexCotas()[1]
    c = elementoIngresado()
    busquedaBinariaCotas(b,c)



def indexNombres(listaPinturas):
    indiceNombres = {}
    indiceNombresOrdenado = {}
    nombres = []
    contador = 0
    
    for i in listaPinturas:
        nombres.append(i['Nombre'])
        indiceNombres[i['Nombre']] = contador
        contador += 1
       
    nombres.sort()    


    for i in nombres:
        for j in indiceNombres:
            if i == j:
                indiceNombresOrdenado[i] = indiceNombres[j]
                break

    tuplaNombres = indiceNombresOrdenado.items()
    tuplaNombres = tuple(tuplaNombres)
    listaNombres = []
    for i in tuplaNombres:
        listaNombres.append(list(i))
    return listaNombres


#Funcion que retorna la lista de nombres pero sin espacios 

def nombresSinEspacios(lista):
    listaSinEspacios = []
    for i in lista:
        elem = ''
        for j in i[0]:
            if j == ' ':
                continue
            else:
                elem += j
        agregar = [elem,i[1]]
        listaSinEspacios.append(agregar)
    return listaSinEspacios
        

#Realizo la busqueda, NO ME FUNCIONA

def busquedaBinariaNombres(lista,elemento3):   
    x = len(lista)
    y = x//2
    z = lista[y][0] 

    if z == elemento3:
        print('Encontrado')
    elif z != elemento3 and len(lista) <= 1:
        print('No esta lo que pusiste')   
    elif len(lista) == 2 and z != elemento3:
        lista2 = lista[0:1]
        busquedaBinariaNombres(lista2)  
    elif elemento3 > z:
        lista2 = lista[y:x+1]
        busquedaBinariaNombres(lista2)  
    elif elemento3 < z:
        lista2 = lista[0:y+1]
        busquedaBinariaNombres(lista2)  
    else:
        pass


#Funcion que se utiliza en el archivo Parte34, me esta fallando

def busquedaBinariaCotas3(lista,elemento):   
    x = len(lista)
    y = x//2
    z = lista[y][0] 
    if z == elemento:
        indice = lista[y][1]       
        return listaPinturas[indice], indice
    elif z != elemento and len(lista) <= 1:
        return False, False
    elif len(lista) == 2 and z != elemento:
        lista2 = lista[0:1]
        busquedaBinariaCotas3(lista2,elemento)  
    elif elemento > z:
        lista2 = lista[y:x+1]
        busquedaBinariaCotas3(lista2,elemento)  
    elif elemento < z:
        lista2 = lista[0:y+1]
        busquedaBinariaCotas3(lista2,elemento)  
    else:
        pass


