import os, time
from funciones import * 
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
        listar_trabajadores()
    elif opc ==3:
        exportar_archivo_txt
    else:
        salida()
    time.sleep(3)    