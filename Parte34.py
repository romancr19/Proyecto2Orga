import DatosPinturas
import json

jsonn = DatosPinturas.cargarDelJson()

listaPinturas = DatosPinturas.nombresCapitalizados()

global listaCotas
listaCotas = DatosPinturas.indexCotas()[1]
global busqueda


#No me funciona, eres libre de cambiarlo o eliminarlo

def mantenimiento():
    entrada = DatosPinturas.elementoIngresado()
    busqueda = DatosPinturas.busquedaBinariaCotas3(listaCotas,entrada)[1]
      
    print(busqueda)
    if busqueda == False:
        print('No existe el elemento insertado')
    else:
        indice = listaCotas[1][busqueda]
        if jsonn[indice]['Status'] == 'EN MANTENIMIENTO':
            print('La pintura ingresada ya esta en mantenimiento')
        else:
            jsonn[indice]['Status'] = 'EN MANTENIMIENTO'



def exhibicion(busqueda,entrada):
    pass