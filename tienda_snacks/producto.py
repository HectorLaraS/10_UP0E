class Producto:
    def __init__(self, id:int = 0, nombre:str = "snack", codigo_barra: str = "7410", precio: float = 0.1):
        self._id = id
        self._nombre = nombre
        self._codigo_barra = codigo_barra
        self._precio = precio

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def nombre(self) -> str:
        return self._nombre
    
    @property
    def codigo_barra(self) -> str:
        return self._codigo_barra
    
    @property
    def precio(self) -> float:
        return self._precio
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @nombre.setter
    def nombre(self, value: str) -> None:
        self._nombre = value


    @precio.setter
    def precio(self, value: float) -> None:
        self._precio = value

    def producto_dict(self) -> dict[str, str | float | int]: 
        return {
            "id": self._id,
            "nombre": self._nombre,
            "codigo_barra": self._codigo_barra,
            "precio": self._precio
        }