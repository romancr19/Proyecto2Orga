import Menu
import DatosPinturas
import json

def main():
    pinturas = DatosPinturas.pinturasCapitalizadas()

    indiceNombres = DatosPinturas.crearIndexNombres(pinturas)
    indiceCotas = DatosPinturas.crearIndexCotas(pinturas)

    Menu.menu(pinturas, indiceNombres, indiceCotas)

main()