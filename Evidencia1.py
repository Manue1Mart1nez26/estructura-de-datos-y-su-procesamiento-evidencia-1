"""
Evidencia 1, Estructura de datos y su procesamiento.

Carlos Manuel Martínez Martínez."""

from collections import namedtuple
from os import remove

Ventas = namedtuple("Ventas",["nombre","correoElectronico"])
DiccionarioVentas = {}
DiccionarioPrecios = {"Programación":[87, 80, 80,20,100], "Base de datos":[71, 100, 70, 100, 100],
"Contabilidad":[99, 57, 57, 100, 100]}

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
        while True:
            clave = int(input("Porfavor ingrese la clave de la Venta: "))
            if clave in DiccionarioVentas.keys():
                print("Ya existe en el diccionario esa clave, intente nuevamente")
            else:
                nombre = input("Porfavor ingrese su nombre: ").capitalize()
                correoElectronico = input("Porfavor introduzca su correo electrónico: ").lower()
                TuplaVenta = Ventas(nombre,correoElectronico)
                DiccionarioVentas[clave] = TuplaVenta
                print(f"\n-- Confirmación de datos:\nClave: {clave}, Nombre: {nombre}, Correo: {correoElectronico}")
                break

    if opcionElegida == 2:#Registrar una venta| 1.2 dentro de este que agregue mas articulos y no solo uno
        while True:
            clave = int(input("Porfavor ingrese la clave de la Venta: "))
            if clave in DiccionarioVentas.keys():
                print("Ya existe en el diccionario esa clave, intente nuevamente")
            else:
                nombre = input("Porfavor ingrese su nombre: ").capitalize()
                correoElectronico = input("Porfavor introduzca su correo electrónico: ").lower()
                TuplaVenta = Ventas(nombre,correoElectronico)
                DiccionarioVentas[clave] = TuplaVenta
                print(f"\n-- Confirmación de datos:\nClave: {clave}, Nombre: {nombre}, Correo: {correoElectronico}")
                break

    if opcionElegida == 3:#Consultar una venta
        if DiccionarioVentas:
            claveBuscado = int(input("Ingrese la clave a buscar: "))
            if claveBuscado in DiccionarioVentas:
                print("\n-- Resultado de búsqueda:")
                print(f"Nombre: {DiccionarioVentas[claveBuscado].nombre}")
                print(f"Correo: {DiccionarioVentas[claveBuscado].correoElectronico}")
            else:
                print("No existe la clave introducida, intente nuevamente")

    if opcionElegida == 4:#Comprobacion de que estan las ventas
        if DiccionarioVentas:
            print("\n-- Listado completo de Ventas")
            print(f'\n{"Clave":<5} | {"Nombre":^18} | {"Correo":<25}')
            for claveCiclo in DiccionarioVentas.keys():
                print(f'{claveCiclo:<5} | {DiccionarioVentas[claveCiclo].nombre:^18} | {DiccionarioVentas[claveCiclo].correoElectronico:<25}')
        else:
            print("No se encuentra ningún registro")

    if opcionElegida == 5:#Eliminacion de ventas
        claveEliminar = int(input('Clave del registro a eliminar: '))

        if claveEliminar in DiccionarioVentas.keys():
            print('\n-- Registor a eliminar:')
            print(f'\n{"Clave":<5} | {"Nombre":^18} | {"Correo":<25}')
            print(f'{claveEliminar:<5} | {DiccionarioVentas[claveEliminar].nombre:^18} | {DiccionarioVentas[claveEliminar].correoElectronico:<25}')
            eliminacion_reg = int(input("\n¿Está seguro de eliminar este registro?\n1) Si\n2) No\n> "))
            if eliminacion_reg == 1:
                del DiccionarioVentas[claveEliminar]
                print(f"Se ha eliminado satisfactoriamente al registro No. {claveEliminar}")
            elif eliminacion_reg == 2:
                print("No se eliminará el registro")
            else:
                print("El dato es inválido")
        else:
            print("No se encuentra la clave introducida")

    if opcionElegida == 6:
        print("Gracias por usar el programa, buen día.")
        break
