import os, time
trabajadores = []
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
        print("-----REGISTRO DE TRABAJADORES-----")
        nombre_apellido =input("Ingrese Nombre y Apellido: ")
        cargo = int(input("Ingrese cargo (1- CEO, 2- DESARROLLADOR, -3 ANALISTA): "))
        sueldo_bruto=int(input("Ingrese sueldo bruto: "))
        desc_salud= int(7/100 * sueldo_bruto)
        desc_afp= int(12/100 *sueldo_bruto)
        sueldo_liquido=int(sueldo_bruto-desc_salud-desc_afp)
        trabajador =[nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_salud,desc_afp,sueldo_liquido]
        trabajadores.append(trabajador)
        print("Trabajador agregaco con exitó...")    

    elif opc ==2:
        pass
    elif opc ==3:
        pass
    else:
        print("Gracias...")
        break
    time.sleep(3)    