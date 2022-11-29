import json

def cargarDelJson():
    with open("pinturas.json", "r") as f:
        jsonString = f.read()
        f.close()
        return json.loads(jsonString)

def guardarJson(pinturas):
    guardar = json.dumps(pinturas, indent= "   ")
    with open("pinturas.json", 'w') as f:
        f.write(guardar)
        f.close()
    return

#Se pone la 1era letra mayuscula de cada nombre de las pinturas    
def pinturasCapitalizadas():
    listaPinturas = cargarDelJson()
    for i in listaPinturas:
        for j in i['Nombre']:
            j.capitalize()
    return listaPinturas

def crearIndexCotas(listaPinturas):
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
    # listaCotas = []
    # for i in tuplaCotas:
    #     listaCotas.append(list(i))

#Se retorna un diccionario de cotas ordenados alfabeticamente con su posicion en el vector principal 
#y en forma de lista    

    return indiceCotasOrdenado

def crearIndexNombres(listaPinturas):
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

    # tuplaNombres = indiceNombresOrdenado.items()
    # tuplaNombres = tuple(tuplaNombres)
    # listaNombres = []
    # for i in tuplaNombres:
    #     listaNombres.append(list(i))
    return indiceNombresOrdenado

def elementoIngresado():
    elemento = input('Ingrese el valor que desea buscar: ')
    print("")
    
    return elemento

def buscarPorCotas(pinturas, indiceCotas):
    cota = elementoIngresado()
    cota = cota.upper()

    cotas = list(indiceCotas.keys())
    indice = busquedaBinaria(cotas, cota)

    if indice == -1:
        print('No se encontro la cota ingresada')
        return
    
    return pinturas[list(indiceCotas.values())[indice]]

def buscarPorNombre(pinturas, indiceNombres):
    nombre = elementoIngresado()

    nombres = list(indiceNombres.keys())
    indice = busquedaBinaria(nombres, nombre)

    if indice == -1:
        print('No se encontro la cota ingresada')
        return
    
    return pinturas[list(indiceNombres.values())[indice]]

def busquedaBinaria(cotas, target):
    left = 0
    right = len(cotas) - 1

    while (left <= right):
        mid = (right + left) // 2

        if cotas[mid] == target:
            return mid
        elif cotas[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
