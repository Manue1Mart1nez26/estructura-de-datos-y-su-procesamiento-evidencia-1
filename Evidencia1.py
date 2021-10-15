"""
Evidencia 1, Estructura de datos y su procesamiento.

Carlos Manuel Martínez Martínez."""
import pandas as pd
from collections import namedtuple
from os import remove

SEPARADOR = ("*" * 20)
Ventas = namedtuple("Ventas",["Articulo","FechaVenta"])
DiccionarioVentas = {}
DiccionarioPrecios = {"Juego de llantas 1":[400], "Juego de llantas 2":[600]}
notas_Precios = pd.DataFrame(DiccionarioPrecios)


while True:
    print("\n-- Bienvenido(a) al Menú")
    print("1) Ver precios")#Lista o menu con los articulos y precios que se visualiza
    print("2) Agregar una Venta") #Registrar una venta| 2.2 dentro de este que agregue mas articulos y no solo uno
    print("3) Búsqueda específica") #Consultar una venta
    print("4) Ver listado completo")#Comprobacion de que estan las ventas que con su unico folio se visualizara los productos de la venta
    print("5) Eliminar una Venta")#Eliminacion de ventas
    print("6) Salir")
    opcionElegida = int(input("> "))

    if opcionElegida == 1: #Lista o menu con los articulos y precios que se visualiza| Cambiar para que se visualize en lo que hay en el DiccionarioPrecios (also cambiar los datos dentro del diccionario)
        if DiccionarioPrecios:
            print(notas_Precios.mean())

    if opcionElegida == 2: #Registrar una venta| .2 dentro de este que agregue mas articulos y no solo uno
        while True:
            folioUnico = int(input("Porfavor ingrese el numero de venta : "))
            if folioUnico in DiccionarioVentas.keys():
                print("Ya existe en el diccionario esa folioUnico, intente nuevamente")
            else:
                Articulo = input("Porfavor ingrese su Articulo: ").capitalize()
                FechaVenta = input("Porfavor introduzca la fecha: ").lower()
                TuplaVenta = Ventas(Articulo,FechaVenta)
                DiccionarioVentas[folioUnico] = TuplaVenta
                print(f"\n-- Confirmación de datos:\nfolioUnico: {folioUnico}, Articulo: {Articulo}, Fecha: {FechaVenta}")
                break

    if opcionElegida == 3:#Consultar una venta
        if DiccionarioVentas:
            folioUnicoBuscado = int(input("Ingrese La venta a buscar: "))
            if folioUnicoBuscado in DiccionarioVentas:
                print("\n-- Resultado de búsqueda:")
                print(f"Articulo: {DiccionarioVentas[folioUnicoBuscado].Articulo}")
                print(f"Fecha: {DiccionarioVentas[folioUnicoBuscado].FechaVenta}")
            else:
                print("No existe La venta introducida, intente nuevamente")

    if opcionElegida == 4:#Comprobacion de que estan las ventas
        if DiccionarioVentas:
            print("\n-- Listado completo de Ventas")
            print(f'\n{"folioUnico":<10} | {"Articulo":^18} | {"Fecha":<25}')
            for folioUnicoCiclo in DiccionarioVentas.keys():
                print(f'{folioUnicoCiclo:<10} | {DiccionarioVentas[folioUnicoCiclo].Articulo:^18} | {DiccionarioVentas[folioUnicoCiclo].FechaVenta:<25}')
        else:
            print("No se encuentra ningún registro")

    if opcionElegida == 5:#Eliminacion de ventas
        folioUnicoEliminar = int(input('folioUnico del registro a eliminar: '))

        if folioUnicoEliminar in DiccionarioVentas.keys():
            print('\n-- Registor a eliminar:')
            print(f'\n{"folioUnico":<10} | {"Articulo":^18} | {"Fecha":<25}')
            print(f'{folioUnicoEliminar:<10} | {DiccionarioVentas[folioUnicoEliminar].Articulo:^18} | {DiccionarioVentas[folioUnicoEliminar].FechaVenta:<25}')
            eliminacion_reg = int(input("\n¿Está seguro de eliminar este registro?\n1) Si\n2) No\n> "))
            if eliminacion_reg == 1:
                del DiccionarioVentas[folioUnicoEliminar]
                print(f"Se ha eliminado satisfactoriamente al registro No. {folioUnicoEliminar}")
            elif eliminacion_reg == 2:
                print("No se eliminará el registro")
            else:
                print("El dato es inválido")
        else:
            print("No se encuentra La venta introducida")

    if opcionElegida == 6:
        print("Gracias por usar el programa, buen día.")
        break
