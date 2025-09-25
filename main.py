# main.py
from bus import Bus
from billete import comprar_interactivo, devolver_interactivo

def pedir_entero(mensaje, minimo=None):
    while True:
        txt = input(mensaje).strip()
        try:
            n = int(txt)
            if minimo is not None and n < minimo:
                print("El valor debe ser como mínimo " + str(minimo) + ".")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Introduzca un número entero.")

def seleccionar_o_crear_bus(buses):
    matricula = input("Introduce la matrícula del bus: ").strip()
    if matricula in buses:
        print("Bus '" + matricula + "' seleccionado.")
        return buses[matricula]

    # Crear nuevo bus con validación de máximo 100 plazas
    while True:
        plazas_max = pedir_entero("Plazas totales del nuevo bus (máx. 100): ", minimo=1)
        if plazas_max > 100:
            print("Un bus no puede tener más de 100 plazas.")
        else:
            break

    nuevo = Bus(plazas_max, matricula)
    buses[matricula] = nuevo
    print("Bus '" + matricula + "' creado con " + str(plazas_max) + " plazas.")
    return nuevo

def mostrar_estado(bus):
    print("\n=== ESTADO DEL BUS ===")
    print("Matrícula      : " + bus.matricula)
    print("Plazas totales : " + str(bus.plazas_max))
    print("Plazas libres  : " + str(bus.get_plazas_libres()))
    print("Plazas vendidas: " + str(bus.plazas_vendidas))
    if bus.registro_clientes:
        print("Clientes con billetes:")
        for nombre, datos in bus.registro_clientes.items():
            print("  - " + nombre + ": " + str(datos["cantidad"]) + " billete(s)")
    else:
        print("No hay clientes con billetes actualmente.")

def main():
    buses = {}        # diccionario: matricula -> Bus
    bus_actual = None

    while True:
        print("\n--- MENÚ ---")
        print("1.- Seleccionar/crear bus por matrícula")
        print("2.- Comprar billetes (del bus seleccionado)")
        print("3.- Devolver billetes (del bus seleccionado)")
        print("4.- Consultar estado (del bus seleccionado)")
        print("5.- Consultar estado de otro bus por matrícula")
        print("0.- Salir")
        opcion = input("Elija una opción: ").strip()

        if opcion == "1":
            bus_actual = seleccionar_o_crear_bus(buses)

        elif opcion == "2":
            if not bus_actual:
                print("Primero seleccione/cree un bus (opción 1).")
                continue
            ok, msg = comprar_interactivo(bus_actual)
            print(msg)
            mostrar_estado(bus_actual)

        elif opcion == "3":
            if not bus_actual:
                print("Primero seleccione/cree un bus (opción 1).")
                continue
            ok, msg = devolver_interactivo(bus_actual)
            print(msg)
            mostrar_estado(bus_actual)

        elif opcion == "4":
            if not bus_actual:
                print("Primero seleccione/cree un bus (opción 1).")
                continue
            mostrar_estado(bus_actual)

        elif opcion == "5":
            if not buses:
                print("No hay buses aún. Cree uno con la opción 1.")
                continue
            mat = input("Matrícula a consultar: ").strip()
            bus = buses.get(mat)
            if not bus:
                print("No existe un bus con matrícula '" + mat + "'.")
            else:
                mostrar_estado(bus)

        elif opcion == "0":
            print("Gracias. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
