from bus import bus
from cliente import cliente 

valor_texto = 0
vender = True

class billete:
    def __init__ (self, cliente:cliente,bus:bus):
        self.bus = bus
        self.cliente = cliente


    def venta_billete(self):
        self.bus.setplazas_max() -= 1
        self.bus.setplazas_vendidas() += 1   
        return self.bus.getplazas_max(), self.bus.getplazas_vendidas()

    def devolucion(self):
        self.bus.setplazas_max() += 1
        self.bus.setplazas_vendidas() -= 1   
        return self.bus.getplazas_max(), self.bus.getplazas_vendidas()
