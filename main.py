# main.py
from bus import Bus
from billete import comprar_interactivo, devolver_interactivo

def pedir_int(mensaje: str, minimo: int = None) -> int:
    while True:
        valor = input(mensaje).strip()
        try:
            n = int(valor)
            if minimo is not None and n < minimo:
                print(f"El valor debe ser como mínimo {minimo}.")
                continue
            return n
        except ValueError:
            print("Entrada inválida. Introduzca un número entero.")

def seleccionar_o_crear_bus(buses: dict) -> Bus:
    matricula = input("Introduce la matrícula del bus: ").strip()
    if matricula in buses:
        print(f"Bus '{matricula}' seleccionado.")
        return buses[matricula]
    # Crear uno nuevo
    plazas_max = pedir_int("Plazas totales del nuevo bus: ", minimo=1)
    nuevo = Bus(plazas_max, matricula)
    buses[matricula] = nuevo
    print(f"Bus '{matricula}' creado con {plazas_max} plazas.")
    return nuevo

def mostrar_estado(bus: Bus):
    print("\n=== ESTADO DEL BUS ===")
    print(f"Matrícula      : {bus.matricula}")
    print(f"Plazas totales : {bus.plazas_max}")
    print(f"Plazas libres  : {bus.plazas_libres}")
    print(f"Plazas vendidas: {bus.plazas_vendidas}")
    # (Opcional) ver últimos clientes:
    if bus.ventas:
        print("Últimas ventas:")
        # Mostramos hasta 5 últimas ventas
        for v in bus.ventas[-5:]:
            print(f"  - {v['cantidad']} billete(s) para {v['cliente'].nombre_completo}")
    else:
        print("No hay ventas registradas.")

def main():
    # Varios buses gestionados por matrícula
    buses = {}
    bus_actual = None  # tipo: Bus | None

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
                print(f"No existe un bus con matrícula '{mat}'.")
            else:
                mostrar_estado(bus)

        elif opcion == "0":
            print("Gracias. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
