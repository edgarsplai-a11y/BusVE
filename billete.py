# billete.py
# Módulo de ayuda para interacción por consola sobre un Bus

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
    try:
        cantidad = int(input("¿Cuántos billetes desea devolver? ").strip())
    except ValueError:
        return False, "Entrada inválida. Debe introducir un número entero en la cantidad."

    ok, msg = bus.devolver_plazas(cantidad)
    return ok, msg
