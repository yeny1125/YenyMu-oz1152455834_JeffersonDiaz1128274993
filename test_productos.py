import os
import unittest

from productos import Producto
from productos import SpaCRUD


class TestSpaCRUD(unittest.TestCase):

    def setUp(self):

        self.archivo_prueba = "test_productos.json"

        self.spa = SpaCRUD(self.archivo_prueba)

        self.producto = Producto(
            1,
            "Aceite",
            "Aceite relajante",
            40000,
            5
        )

    def tearDown(self):

        if os.path.exists(self.archivo_prueba):
            os.remove(self.archivo_prueba)

    def test_crear_producto(self):

        self.spa.crear_producto(self.producto)

        productos = self.spa.obtener_productos()

        self.assertEqual(len(productos), 1)

    def test_crear_producto_repetido(self):

        self.spa.crear_producto(self.producto)

        with self.assertRaises(ValueError):
            self.spa.crear_producto(self.producto)

    def test_obtener_productos(self):

        self.spa.crear_producto(self.producto)

        productos = self.spa.obtener_productos()

        self.assertEqual(
            productos[0]["nombre"],
            "Aceite"
        )

    def test_actualizar_producto(self):

        self.spa.crear_producto(self.producto)

        self.spa.actualizar_producto(
            1,
            precio=50000
        )

        productos = self.spa.obtener_productos()

        self.assertEqual(
            productos[0]["precio"],
            50000
        )

    def test_actualizar_producto_error(self):

        with self.assertRaises(ValueError):
            self.spa.actualizar_producto(
                999,
                precio=1000
            )

    def test_eliminar_producto(self):

        self.spa.crear_producto(self.producto)

        self.spa.eliminar_producto(1)

        productos = self.spa.obtener_productos()

        self.assertEqual(
            len(productos),
            0
        )

    def test_eliminar_producto_error(self):

        with self.assertRaises(ValueError):
            self.spa.eliminar_producto(999)


if __name__ == "__main__":
    unittest.main()