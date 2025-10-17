from tienda.ticket import *
from tienda.producto import *
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent          # .../prod
ROOT = HERE.parent                              # .../tienda
DB_FILE = ROOT / "storage" / "catalogo.json"
DB_FILE_TICKETS = ROOT / "storage" / "tickets_compras.json"

def test():
    print("Hola Mundo")

BANNER_PRINCIPAL = """
1) MOSTRAR CATALOGO
2) COMPRAR PRODUCTO
3) MOSTRAR TICKET
4) SALIR
"""

def validar_entrada():
    output = None
    while True:
        entrada = input("Ingrese su eleccion: ")
        try:
            output = int(entrada)
            break
        except:
            print("OPCION NO VALIDA!!!")
    return output

def get_catalogo_productos():
    lst_catalogo_productos = []
    with open(DB_FILE,"r") as json_file:
        lst_catalogo_productos = json.load(json_file)
    return lst_catalogo_productos

def get_solo_ids():
    lst_ids = []
    lst_productos = get_catalogo_productos()
    for producto in lst_productos:
        lst_ids.append(producto.get("id"))
    return lst_ids


def get_ticket_id():
    new_id = None
    with open(DB_FILE_TICKETS,"r") as json_file:
        lst_ticket = json.load(json_file)
        if len(lst_ticket) == 0:
            new_id = 1
        else:
            for ticket in lst_ticket:
                new_id = ticket.get("id") + 1
    return new_id

def get_ticket_list():
    with open(DB_FILE_TICKETS,"r") as json_file:
        lst_tickets = json.load(json_file)
    return lst_tickets

def update_ticket(new_ticket):
    lst_tickets: list = get_ticket_list()
    lst_tickets.append(new_ticket)
    with open(DB_FILE_TICKETS,"w") as json_file:
        json.dump(lst_tickets,json_file,indent=4)

def main():
    new_ticket = Ticket()
    lst_producto = get_catalogo_productos()
    new_ticket.id = get_ticket_id()
    salir = False
    while not salir:
        print(BANNER_PRINCIPAL)
        eleccion = validar_entrada()
        if eleccion == 1:
            producto_tmp = Producto()
            for tmp_prod in lst_producto:
                producto_tmp.id = tmp_prod.get("id")
                producto_tmp.nombre = tmp_prod.get("nombre")
                producto_tmp.precio = tmp_prod.get("precio")
                print(producto_tmp.__str__())
        if eleccion == 2:
            producto_to_add = Producto()
            lst_ids = get_solo_ids()
            while True:
                print("Selecciona Producto \n")
                producto_comprado = validar_entrada()
                if producto_comprado in lst_ids:
                    break
            for producto_buscado in lst_producto:
                if producto_comprado == producto_buscado.get("id"):
                    producto_to_add.id = producto_buscado.get("id")
                    producto_to_add.nombre = producto_buscado.get("nombre")
                    producto_to_add.codigo_barra = producto_buscado.get("codigo_barra")
                    producto_to_add.precio = producto_buscado.get("precio")
                    print("PRODUCTO AGREGADO AL CARRITO!!! \n")
                    new_ticket.agregar_producto(producto_to_add.producto_dict())
                    new_ticket.agregar_producto_str(producto_to_add.__str__())
                    new_ticket.get_total()

        if eleccion == 3:
            print(f"Ticket ID: {new_ticket.id}")
            print(f"Total hasta el momento {new_ticket.total}")
            print("PRODUCTOS EN CARRITO".center(50,"*"))
            for producto in new_ticket.productos_str:
                print(producto)
        if eleccion == 4:
            print(f"Su total es de ${new_ticket.total}, favor de pagar en caja con el numero de ticket {new_ticket.id}")
            update_ticket(new_ticket.ticket_dict())
            print("ADIOS!!!")
            salir = True

if __name__ == "__main__":
    """ print(validar_entrada()) """
    main()
    """ tmp = get_catalogo_productos()
    print(tmp) """
    """ get_ticket_id() """