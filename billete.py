from bus import Bus
from cliente import Cliente

def comprar_interactivo(bus: Bus):
    try:
        nombre = input("Nombre del cliente: ").strip()
        apellido = input("Apellido del cliente: ").strip()
        cantidad = int(input("¿Cuántos billetes desea comprar? ").strip())
    except ValueError:
        return False, "Entrada inválida. Debe introducir un número entero en la cantidad."

    if not nombre or not apellido:
        return False, "Nombre y apellido son obligatorios."

    cliente = Cliente(nombre, apellido)
    ok, msg = bus.vender_plazas(cantidad, cliente)
    return ok, msg

def devolver_interactivo(bus: Bus):
    if not bus.tickets_por_cliente:
        return False, "No hay clientes con billetes comprados."

    print("Clientes con billetes:")
    clientes = list(bus.tickets_por_cliente.items())
    for i, (cliente, cant) in enumerate(clientes, start=1):
        print(f"{i}. {cliente.nombre_completo} ({cant} billete(s))")

    try:
        idx = int(input("Seleccione el cliente por número: ").strip())
        if idx < 1 or idx > len(clientes):
            return False, "Selección inválida."
    except ValueError:
        return False, "Entrada inválida."

    cliente, max_cant = clientes[idx - 1]

    try:
        cantidad = int(input(f"¿Cuántos billetes desea devolver (máx {max_cant})? ").strip())
    except ValueError:
        return False, "Entrada inválida."

    if cantidad < 1 or cantidad > max_cant:
        return False, f"Cantidad inválida. Solo puede devolver entre 1 y {max_cant}."

    ok, msg = bus.devolver_plazas(cantidad, cliente)
    return ok, msg 
