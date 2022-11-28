

import json
from DatosPinturas import *
from Parte34 import *



def cargarDelJson():
    with open("pinturas.json", "r") as f:
        jsonString = f.read()
        return json.loads(jsonString)
    
cargarDelJson()
listaPinturas = nombresCapitalizados()


""" 
Definimos el menu, aca es donde el usuario tiene 6 opciones para manipular el gestor de pinturas
"""


def menu():


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
#En case 1, permitimos que el usuario registre una nueva pintura, tomando Deleted como false por defecto
            
            case '1':
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
                       
                        if (len(cota) != 8) or (cantidad_digitos != 4 and cantidad_caracteres != 4) or ' ' in cota:
                            raise Exception
                            
                        pintura['Cota'] = cota
                        
                        nombre = input('Ingrese el nombre de la pintura. Maximo 30 caracteres: ')
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
                        
                        
                        listaPinturas.append(pintura)

                        guardar = json.dumps(listaPinturas, indent= "   ")
                        with open("pinturas.json", 'w') as f:
                            f.write(guardar)
                            f.close()
   
                        break
                    except:
                        print("Ocurrio un error, pero vuelvanlo a intentar")

# Aca, tomamos la opcion de busqueda binaria por cota y por nombre. Falta por nombre
            case '2':   
                opcion2 = input('''Ingrese 1 para consultar pintura por Cota.
Ingrese 2 para consultar pintura por Nombre: ''')
                match opcion2: 
                    case '1': 
                        coticas()
                    case '2': 
                        pass
                    case other: 
                        print('Ingreso no valido')

                        
#Para cambiar a mantenimiento. No me funciona

            case '3': 
                x = indexCotas()
                opcion3 = input('''Ingrese 1 para poner en mantenimiento una pintura mediante la busqueda por cota
Ingrese 2 para poner en mantenimiento una pintura mediante la busqueda por nombre: ''')
                match opcion3:
                    case '1': 
                        mantenimiento()
                    case '2': 
                        pass
                    case other:
                        print('Opcion no valida')
                      

            case 4: 
                pass
            case 5: 
                pass
            case 6: 
                pass
            case other: 
                print('Ninguna de las opciones es valida')


menu()                


                





