trabajadores = []
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
    pass
def exportar_archivo_txt():
    pass
def salida():
    print("Gracias...")
    exit()
