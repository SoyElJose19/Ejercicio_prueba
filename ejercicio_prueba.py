from funciones import * 
import csv
import os
import time 

os.system("cls")



nombres_trabajadores=[]
apellidos_trabajadores=[]
cargos_trabajadores=[]
sueldos_trabajadores=[]



while True:

    print("""\tmenú
    1). Registrar trabajador
    2). Lista de todos los trabajadores
    3). imprimir planilla de sueldos
    4). salir del programa""")

    opc=int(input("\tingrese una opción: "))
    if opc in (1,2,3,4):
        break
    else:
        print("error!, debe ingresar una opción disponible (1,2,3,4)")
    
if opc==1:
    print("Registrar trabajador ")
    nombre=input("ingrese el nombre del trabajador: ")
    if nombre:
        pass
    else:
        print("error!, el nombre a ingresar debe ser mayor a 2 letras!")

    apellido=input("ingrese el apellido del trabajador: ")
    if apellido:
        pass
    else:
        print("error!, el nombre a ingresar debe ser mayor a 2 letras!")

    cargo=input("ingrese el cargo del trabajador: ")
    if cargo:
        pass
    else:
        print("error!, el nombre a ingresar debe ser mayor a 2 letras!")
    while True:
        try:
            sueldo_bruto=int(input("ingrese el sueldo bruto del trabajador: "))
            if sueldo_bruto >=100000:
                break
            else:
                print("error!, debe ingresar un sueldo bruto de minimo 100000! ")
        except:
            print("error!, debe ingresar un número entero!")

            nombres_trabajadores.append(nombre)
            apellidos_trabajadores.append(apellido)
            cargos_trabajadores.append(cargo)
            sueldos_trabajadores.append(sueldo_bruto)
            print("trabajador registrado con exito! ")

elif opc==2:
    print("lista de todos los trabajadores: ")
    print(nombres_trabajadores)
    pass
elif opc==3:
    print("imprimir planilla de sueldos: ")
    print(sueldos_trabajadores)
    sueldo_liquido=sueldos_trabajadores*-0.07*-0.12
    print(sueldo_liquido)

    pass
elif opc==4:
    print("salir del programa: ")
    print("hasta luego")

time.sleep(2)





