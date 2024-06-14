import csv
nombres_trabajadores=[]
apellidos_trabajadores=[]
cargos_trabajadores=[]
sueldos_trabajadores=[]

def datos_del_trabajador():
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

def lista_de_los_trabajadores():
    print("lista de todos los trabajadores: ")
    print(nombres_trabajadores)
    pass

def imprimir_planilla_de_sueldos():
    print("imprimir planilla de sueldos: ")
    print(sueldos_trabajadores)
    sueldo_liquido=sueldos_trabajadores*-0.07*-0.12
    print(sueldo_liquido)

def salir_del_programa():
    print("salir del programa: ")
    print("hasta luego")

