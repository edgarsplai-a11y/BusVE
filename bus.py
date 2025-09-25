
from cliente import Cliente

class Bus:
    def __init__(self, plazas_max, matricula):
        if plazas_max < 1 or plazas_max > 100:
            raise ValueError("El número de plazas debe estar entre 1 y 100.")
        self.plazas_max = plazas_max
        self.matricula = matricula
        self.plazas_vendidas = 0
        self.registro_clientes = {}

    def get_plazas_libres(self):
        return self.plazas_max - self.plazas_vendidas

    def vender_plazas(self, cantidad, cliente):
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        libres = self.get_plazas_libres()
        if cantidad > libres:
            return False, "No hay suficientes plazas. Libres: " + str(libres) + "."

        self.plazas_vendidas += cantidad
        nombre = cliente.nombre_completo()
        if nombre in self.registro_clientes:
            self.registro_clientes[nombre]["cantidad"] += cantidad
        else:
            self.registro_clientes[nombre] = {"cliente": cliente, "cantidad": cantidad}

        return True, "Venta realizada: " + str(cantidad) + " billete(s) para " + nombre + "."

    def devolver_plazas(self, cantidad, cliente):
        if cantidad <= 0:
            return False, "La cantidad debe ser mayor que 0."
        nombre = cliente.nombre_completo()
        if nombre not in self.registro_clientes:
            return False, nombre + " no tiene billetes comprados."
        actuales = self.registro_clientes[nombre]["cantidad"]
        if cantidad > actuales:
            return False, nombre + " solo tiene " + str(actuales) + " billete(s)."

        self.plazas_vendidas -= cantidad
        self.registro_clientes[nombre]["cantidad"] -= cantidad
        if self.registro_clientes[nombre]["cantidad"] == 0:
            del self.registro_clientes[nombre]

        return True, "Devolución realizada: " + str(cantidad) + " billete(s) de " + nombre + "."
