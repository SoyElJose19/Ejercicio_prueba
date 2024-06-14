trabajadores = []
cargos=("CEO","DESARROLLADOR","ANALISTA")
def registrar_trabajador():
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

def listar_trabajadores():
    if len(listar_trabajadores)==0:
        print("lista vacia, registre un trabajador en la opción 1...")
    else:
        print("\tLista de trabajadores")
        for t in trabajadores:
            print(f"NOMBRE: {t[0]}\n CARGO: {t[1]} \nBRUTO: {t[2]} \nSALUD: {t[3]} \nAFP: {t[4]} \nLIQUIDO: {t[5]}")
def exportar_archivo_txt():
    pass
def salida():
    print("Gracias...")
    exit()
