import unittest
from tienda.producto import *

class TestProducto(unittest.TestCase):
    def test_obtener_producto_id(self):
        test_product = Producto(
            id=1,
            nombre="Jamon 850g",
            precio=85.0,
            codigo_barra="7410"
        )
        self.assertEqual(test_product.id,1)

    def test_obtener_producto_nombre(self):
        test_product = Producto(
            id=1,
            nombre="Jamon 850g",
            precio=85.0,
            codigo_barra="7410"
        )
        self.assertEqual(test_product.nombre,"Jamon 850g")

if __name__ == "__main__":
    unittest.main() 