import Menu
import DatosPinturas
import json

def main():
    y = DatosPinturas.nombresCapitalizados()
    x = DatosPinturas.indexNombres(y)
    print(x)
    Menu.cargarDelJson()
    Menu.menu()
    

main()