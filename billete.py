# billete.py
from bus import Bus
from cliente import Cliente

def _leer_entero(msg):
    txt = input(msg).strip()
    try:
        return int(txt), None
    except ValueError:
        return None, "Entrada inválida. Debe introducir un número entero."

def comprar_interactivo(bus):
    nombre = input("Nombre del cliente: ").strip()
    apellido = input("Apellido del cliente: ").strip()
    if not nombre or not apellido:
        return False, "Nombre y apellido son obligatorios."
    cantidad, err = _leer_entero("¿Cuántos billetes desea comprar? ")
    if err:
        return False, err
    cliente = Cliente(nombre, apellido)
    return bus.vender_plazas(cantidad, cliente)

def devolver_interactivo(bus):
    nombre = input("Nombre del cliente: ").strip()
    apellido = input("Apellido del cliente: ").strip()
    if not nombre or not apellido:
        return False, "Nombre y apellido son obligatorios."
    cantidad, err = _leer_entero("¿Cuántos billetes desea devolver? ")
    if err:
        return False, err
    cliente = Cliente(nombre, apellido)
    return bus.devolver_plazas(cantidad, cliente)
