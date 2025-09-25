from typing import List, Dict, Any
from cliente import Cliente

class Bus:
    def __init__(self, plazas_max: int, matricula: str):
        self.plazas_max = plazas_max
        self.matricula = matricula
        self.plazas_vendidas = 0
        self.ventas: List[Dict[str, Any]] = []  
        self.devoluciones: List[Dict[str, Any]] = []  
        self.tickets_por_cliente: Dict[Cliente, int] = {}

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
        self.tickets_por_cliente[cliente] = self.tickets_por_cliente.get(cliente, 0) + cantidad

        return True, f"Venta realizada: {cantidad} billete(s) para {cliente.nombre_completo}."

    def devolver_plazas(self, cantidad: int, cliente: Cliente):
        """Devuelve 'cantidad' de plazas de un cliente concreto."""
        if cliente not in self.tickets_por_cliente:
            return False, f"El cliente {cliente.nombre_completo} no tiene billetes comprados."
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        if cantidad > self.tickets_por_cliente[cliente]:
            return False, f"{cliente.nombre_completo} solo tiene {self.tickets_por_cliente[cliente]} billete(s)."

        self.plazas_vendidas -= cantidad
        self.tickets_por_cliente[cliente] -= cantidad
        if self.tickets_por_cliente[cliente] == 0:
            del self.tickets_por_cliente[cliente]

        self.devoluciones.append({"cliente": cliente, "cantidad": cantidad})
        return True, f"Devolución realizada: {cantidad} billete(s) de {cliente.nombre_completo}."
