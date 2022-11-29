import json
from DatosPinturas import *


""" 
Definimos el menu, aca es donde el usuario tiene 6 opciones para manipular el gestor de pinturas
"""



def menu(pinturas, indiceNombres, indiceCotas):
    print('''BIENVENIDO AL GESTOR DE PINTURAS PARA EL MUSEO LOUVRE
A continuacion, le presentaremos unas opciones para gestionar nuestro programa''')

    while True:
        decision = input('''Ingrese 1 para insertar una nueva pintura. 
Ingrese 2 para consultar una nueva pintura
Ingrese 3 para colocar en mantenimiento una de nuestras pinturas
Ingrese 4 para colocar en exhibicion una de nuestras pinturas
Ingrese 5 para eliminar logicamente una pintura del sistema
Ingrese 6 para eliminar fisicamente alguna pintura eliminada logicamente
Ingrese opcion: ''')

        n = ['1','2','3','4','5','6']
        while not decision in n:
            decision = input('Ingrese una decision valida: ')            


        match decision:
            case '1':
                crearPintura(pinturas)

            case '2':   
                consultarPintura(pinturas, indiceNombres, indiceCotas)

            case '3': 
                mantenimientoPintura(pinturas, indiceNombres, indiceCotas)
            
            case '4': 
                exhibicionPintura(pinturas, indiceNombres, indiceCotas)

            case '5': 
                eliminarLogicamente(pinturas, indiceNombres, indiceCotas)
    
            case '6': 
                eliminarFisicamente(pinturas, indiceNombres, indiceCotas)

            case other: 
                print('Ninguna de las opciones es valida')

        print("")

def crearPintura(pinturas):
    while True:
        try:
            pintura = {'Cota':'','Nombre':'', 'Precio':'', 'Status':'', 'Deleted': False}

            cota = input('''Ingrese la cota de la pintura que desea registrar. 
Recuerde que debe contener 4 numeros y 4 letras: ''')
            cantidad_digitos = 0
            cantidad_caracteres = 0
            cota = cota.upper()

            for c in cota:
                if c.isdigit():
                    cantidad_digitos += 1
                elif c.isalpha():
                    cantidad_caracteres += 1
                else:
                    pass
                        
                        #TODO: Verificar que la cota de la pnituraa unico
            if (len(cota) != 8) or (cantidad_digitos != 4 and cantidad_caracteres != 4) or ' ' in cota:
                raise Exception
                            
            pintura['Cota'] = cota
                        
            nombre = input('Ingrese el nombre de la pintura. Maximo 30 caracteres: ')
                        #TODO: Verificar que el nombre de la cota sea unico
            if len(nombre)>30:
                raise Exception
                        
            pintura['Nombre'] = nombre.capitalize()

            precio = input('Precio de la obra ($): ')
            while not (precio.isnumeric() > 0) or not precio.isnumeric():
                raise Exception
                                
            pintura['Precio'] = precio

            status = input('Ingrese el status de la obra (1 si esta EN EXHIBICION, 2 si esta EN MANTENIMIENTO): ')
            if status != '1' and status != '2':
                raise Exception
                        
            if status == '1':
                pintura['Status'] = 'EN EXHIBICION'
            else:
                pintura['Status'] = 'EN MANTENIMIENTO'
                        
                        
            pinturas.append(pintura)
            guardarJson(pinturas)

            break
        except:
            print("Ocurrio un error, pero vuelvanlo a intentar")

def exhibicionPintura(pinturas, indiceNombres, indiceCotas):
    opcion2 = input('''Ingrese 1 para poner en exhibicion una pintura mediante la busqueda por cota: 
Ingrese 2 para poner en exhibicion una pintura mediante la busqueda por nombre: ''')
                
    pintura = None
    match opcion2:
        case '1': 
            pintura = buscarPorCotas(pinturas, indiceCotas)
        case '2': 
            pintura = buscarPorNombre(pinturas, indiceNombres)
        case other: 
            print('Ingreso no valido')
                
    if pintura:
        if pintura['Status'] == 'EN EXHIBICION':
            print('La pintura ya se encuentra en mantenimiento')
        else:
            pintura['Status'] = 'EN EXHIBICION'  
                        
            print(f'''Cota: {pintura['Cota']}
    Nombre: {pintura['Nombre']}
    Precio: {pintura['Precio']}
    Status: {pintura['Status']}
    Deleted: {pintura['Deleted']}''')
                    
            guardarJson(pinturas)

def mantenimientoPintura(pinturas, indiceNombres, indiceCotas):
    opcion2 = input('''Ingrese 1 para poner en mantenimiento una pintura mediante la busqueda por cota: 
Ingrese 2 para poner en mantenimiento una pintura mediante la busqueda por nombre: ''')
                
    pintura = None
    match opcion2:
        case '1': 
            pintura = buscarPorCotas(pinturas, indiceCotas)
        case '2': 
            pintura = buscarPorNombre(pinturas, indiceNombres)
        case other: 
            print('Ingreso no valido')
                
    if pintura:
        if pintura['Status'] == 'EN MANTENIMIENTO':
            print('La pintura ya se encuentra en mantenimiento')
        else:
            pintura['Status'] = 'EN MANTENIMIENTO'  
                        
            print(f'''Cota: {pintura['Cota']}
    Nombre: {pintura['Nombre']}
    Precio: {pintura['Precio']}
    Status: {pintura['Status']}
    Deleted: {pintura['Deleted']}''')
                    
            guardarJson(pinturas)

def consultarPintura(pinturas, indiceNombres, indiceCotas):
    opcion2 = input('''Ingrese 1 para consultar pintura por Cota:
Ingrese 2 para consultar pintura por Nombre: ''')
    pintura = None
    match opcion2: 
        case '1': 
            pintura = buscarPorCotas(pinturas, indiceCotas)
        case '2': 
            pintura = buscarPorNombre(pinturas, indiceNombres)
        case other: 
            print('Ingreso no valido')
                
    if pintura:
        print(f'''Cota: {pintura['Cota']}
Nombre: {pintura['Nombre']}
Precio: {pintura['Precio']}
Status: {pintura['Status']}
Deleted: {pintura['Deleted']}''')

def eliminarLogicamente(pinturas, indiceNombres, indiceCotas):
    opcion2 = input('''Ingrese 1 para eliminar una pintura mediante la busqueda por cota: 
Ingrese 2 para eliminar una pintura mediante la busqueda por nombre: ''')
                
    pintura = None
    match opcion2:
        case '1': 
            pintura = buscarPorCotas(pinturas, indiceCotas)
        case '2': 
            pintura = buscarPorNombre(pinturas, indiceNombres)
        case other: 
            print('Ingreso no valido')
                
    if pintura:
        if pintura['Deleted'] == True:
            print('La pintura ya se encuentra eliminada')
        else:
            pintura['Deleted'] = True
                        
            print(f'''Cota: {pintura['Cota']}
    Nombre: {pintura['Nombre']}
    Precio: {pintura['Precio']}
    Status: {pintura['Status']}
    Deleted: {pintura['Deleted']}''')
                    
            guardarJson(pinturas)

def eliminarFisicamente(pinturas, indiceNombres, indiceCotas):
    #Delete all the paintings that are logically deleted
    pinturas = [pintura for pintura in pinturas if pintura['Deleted'] == False]
    guardarJson(pinturas)

    #Rebuild the index
    indiceNombres = {}
    indiceCotas = {}
    for i in range(len(pinturas)):
        pintura = pinturas[i]
        indiceNombres[pintura['Nombre']] = i
        indiceCotas[pintura['Cota']] = i

    print('Se eliminaron las pinturas logicamente eliminadas')