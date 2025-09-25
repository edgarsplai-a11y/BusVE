class Cliente:
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()

    @property
    def nombre_completo(self) -> str:
        return f"{self.nombre} {self.apellido}"

    def __repr__(self) -> str:
        return f"Cliente({self.nombre_completo})" 
