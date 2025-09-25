# bus.py
from typing import List, Dict, Any
from cliente import Cliente

class Bus:
    def __init__(self, plazas_max: int, matricula: str):
        self.plazas_max = plazas_max
        self.matricula = matricula
        self.plazas_vendidas = 0
        # Historial simple de ventas y devoluciones
        # ventas: lista de dicts {'cliente': Cliente, 'cantidad': int}
        self.ventas: List[Dict[str, Any]] = []
        # devoluciones: lista de dicts {'cantidad': int}
        self.devoluciones: List[Dict[str, Any]] = []

    @property
    def plazas_libres(self) -> int:
        return self.plazas_max - self.plazas_vendidas

    def vender_plazas(self, cantidad: int, cliente: Cliente):
        """Vende 'cantidad' de plazas a un cliente. Retorna (ok: bool, mensaje: str)."""
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        if cantidad > self.plazas_libres:
            return False, f"No hay suficientes plazas. Libres: {self.plazas_libres}."
        self.plazas_vendidas += cantidad
        self.ventas.append({"cliente": cliente, "cantidad": cantidad})
        return True, f"Venta realizada: {cantidad} billete(s) para {cliente.nombre_completo}."

    def devolver_plazas(self, cantidad: int):
        """Devuelve 'cantidad' de plazas (no asociadas a un cliente concreto)."""
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        if cantidad > self.plazas_vendidas:
            return False, f"No puedes devolver más de las vendidas ({self.plazas_vendidas})."
        self.plazas_vendidas -= cantidad
        self.devoluciones.append({"cantidad": cantidad})
        return True, f"Devolución realizada: {cantidad} billete(s)."
