import random
import math
import csv

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

sueldos = []

def asignar_sueldos():
    global sueldos
    sueldos = [random.randint(300000, 2500000) for _ in range(10)]
    print("\nSueldos asignados con éxito.")
    
def clasificacion_sueldos():
    print("Sueldos inferior a $800.000 //TOTAL:", len([s for s in sueldos if s < 800000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo < 800000:
            print(f"Nombre trabajador: {trabajador} / Sueldo: ${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000 //TOTAL:", len([s for s in sueldos if 800000 <= s <= 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if 800000 <= sueldo <= 2000000:
            print(f"Nombre trabajador: {trabajador} / Sueldo: ${sueldo}")
    
    print("\nSueldos superiores a $2.000.000 TOTAL:", len([s for s in sueldos if s > 2000000]))
    for trabajador, sueldo in zip(trabajadores, sueldos):
        if sueldo > 2000000:
            print(f"Nombre trabajador: {trabajador} / Sueldo: ${sueldo}")
    
    print("\nTOTAL SUELDOS TRABAJADORES:", sum(sueldos))

def estadisticas():
    sueldo_min = min(sueldos)
    sueldo_max = max(sueldos)
    promedio_sueldo = sum(sueldos) / len(sueldos)
    sueldo_geom = math.exp(sum(math.log(sueldo) for sueldo in sueldos) / len(sueldos))
    
    print("\nEstadisticas de sueldo: ")
    print(f"\nEl saldo más alto es: ${sueldo_max}")
    print(f"El saldo más bajo es: ${sueldo_min}")
    print(f"El promedio de sueldos es: ${promedio_sueldo:.2f}")
    print(f"La media geométrica de sueldos es: ${sueldo_geom:.2f}")

def reporte_sueldos():
    with open('reporte_sueldos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Nombre empleado", "Sueldo Base", "Descuento Salud", "Descuento AFP", "Sueldo Líquido"])
        for trabajador, sueldo in zip(trabajadores, sueldos):
            descuento_salud = sueldo * 0.07
            descuento_afp = sueldo * 0.12
            sueldo_liquido = sueldo - descuento_salud - descuento_afp
            writer.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
            print(f"\nNombre empleado: {trabajador} Sueldo Base: ${sueldo} Descuento Salud: ${descuento_salud:.2f} Descuento AFP: ${descuento_afp:.2f} Sueldo Líquido: ${sueldo_liquido:.2f}")

def salir_programa():
    print("\nFinalizando programa...")
    print("Desarrollado por: Dario Gutiérrez Ormeño.")
    print("Rut: 19.960.526-7")

def menu():
    while True:
        print("\nMenu:")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Generar reporte de sueldos")
        print("5. Salir del programa")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            asignar_sueldos()
        elif opcion == 2:
            clasificacion_sueldos()
        elif opcion == 3:
            estadisticas()
        elif opcion == 4:
            reporte_sueldos()
        elif opcion == 5:
            salir_programa()
            break
        else:
            print("Opción no válida. Ingrese una opcion mostrada en pantalla.")

if __name__ == "__main__":
    menu()