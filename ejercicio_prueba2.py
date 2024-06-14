import os, time
from funciones import *

cargos=("CEO","DESARROLLADOR","ANALISTA")
while True:
    os.system("cls")
    print("MENÚ TRABAJADORES")
    print("1.- Registrar Trabajador")
    print("2.- Listar todos los trabajadores")
    print("3.- Imprimir planilla de sueldos")
    print("4.- Salir")
    opc=int(input("Ingrese opción: "))
    os.system("cls")
    if opc ==1:
        registrar_trabajador()
    elif opc ==2:
        pass
    elif opc ==3:
        pass
    else:
        salida()
    time.sleep(3)    