# cliente.py
class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()

    def nombre_completo(self):
        return (self.nombre + " " + self.apellido).strip()

    def __repr__(self):
        return "Cliente(" + self.nombre_completo() + ")"
