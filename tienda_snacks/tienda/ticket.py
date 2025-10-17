from datetime import datetime
from tienda.producto import *

class Ticket:
    def __init__(self, id:int=0, fecha:datetime=datetime.now(), total:float=0.0, productos:list[dict] = [], productos_str: list = []):
        self._id:int = id
        self._fecha:datetime = fecha
        self._total:float = total
        self._productos:list[dict] = productos
        self._productos_str: list[str] = productos_str

    @property
    def id(self) -> int:
        return self._id
    
    @property
    def fecha(self) -> datetime:
        return self._fecha
    
    @property
    def total(self) -> float:
        return self._total
    
    @property
    def productos(self) -> list[dict]:
        return self._productos
    
    @property
    def productos_str(self) -> list[str]:
        return self._productos_str
    
    @id.setter
    def id(self, value: int) -> None:
        self._id = value

    @fecha.setter
    def fecha(self, value: datetime) -> None:
        self._fecha = value

    @total.setter
    def total(self, value: float) -> None:
        self._total = value

    @productos.setter
    def productos(self, value:list) -> None:
        self._productos = value

    @productos_str.setter
    def productos_str(self, value:[list]) -> None:
        self._productos_str = value

    def agregar_producto(self, new_product):
        self._productos.append(new_product)

    def agregar_producto_str(self, new_product):
        self._productos_str.append(new_product)

    def ticket_dict(self):
        return {
            "id":self._id,
            "fecha":self._fecha.strftime("%d/%m/%Y %H:%M:%S"),
            "total":self._total,
            "productos:":self._productos
        }
    
    def get_total(self):
        for producto in self._productos:
            self._total += producto.get("precio")
        round(self._total,2)

    
if __name__ == "__main__":
    ticket_1 = Ticket()
    print(ticket_1.ticket_dict())