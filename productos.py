import json
import os


class Producto:
    def __init__(self, id_producto, nombre, descripcion, precio, cantidad):
        self.id = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "cantidad": self.cantidad
        }


class SpaCRUD:

    def __init__(self, archivo="productos.json"):
        self.archivo = archivo

        # Crear archivo si no existe
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def leer_productos(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []

    def guardar_productos(self, productos):
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(productos, f, indent=4, ensure_ascii=False)

    def crear_producto(self, producto):

        # VALIDACIONES (mejora importante para SonarQube)
        if producto.precio <= 0:
            raise ValueError("El precio debe ser mayor que cero")

        if producto.cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")

        productos = self.leer_productos()

        # Validar duplicados
        if any(p["id"] == producto.id for p in productos):
            raise ValueError("El producto ya existe")

        productos.append(producto.to_dict())
        self.guardar_productos(productos)

    def obtener_productos(self):
        return self.leer_productos()

    def actualizar_producto(
        self,
        id_producto,
        nombre=None,
        descripcion=None,
        precio=None,
        cantidad=None
    ):

        productos = self.leer_productos()

        for producto in productos:

            if producto["id"] == id_producto:

                if nombre is not None:
                    producto["nombre"] = nombre

                if descripcion is not None:
                    producto["descripcion"] = descripcion

                if precio is not None:
                    if precio <= 0:
                        raise ValueError("El precio debe ser mayor que cero")
                    producto["precio"] = precio

                if cantidad is not None:
                    if cantidad < 0:
                        raise ValueError("La cantidad no puede ser negativa")
                    producto["cantidad"] = cantidad

                self.guardar_productos(productos)
                return

        raise ValueError("Producto no encontrado")

    def eliminar_producto(self, id_producto):

        productos = self.leer_productos()

        nuevos_productos = [
            p for p in productos
            if p["id"] != id_producto
        ]

        if len(nuevos_productos) == len(productos):
            raise ValueError("Producto no encontrado")

        self.guardar_productos(nuevos_productos)