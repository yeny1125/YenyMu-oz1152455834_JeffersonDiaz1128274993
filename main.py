from productos import Producto, SpaCRUD

spa = SpaCRUD()


def mostrar_menu():

    print("\n===== SPA CRUD =====")
    print("1. Crear producto")
    print("2. Ver productos")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")


while True:

    mostrar_menu()

    opcion = input("Seleccione una opción: ")

    # CREAR
    if opcion == "1":

        try:
            id_producto = int(input("ID: "))
            nombre = input("Nombre: ")
            descripcion = input("Descripción: ")
            precio = float(input("Precio: "))
            cantidad = int(input("Cantidad: "))

            producto = Producto(
                id_producto,
                nombre,
                descripcion,
                precio,
                cantidad
            )

            spa.crear_producto(producto)

            print("Producto creado correctamente")

        except ValueError as e:
            print("Error:", e)

    # LEER
    elif opcion == "2":

        productos = spa.obtener_productos()

        if len(productos) == 0:
            print("No hay productos registrados")

        else:

            print("\n===== LISTA DE PRODUCTOS =====")

            for producto in productos:

                print(f"""
ID: {producto['id']}
Nombre: {producto['nombre']}
Descripción: {producto['descripcion']}
Precio: ${producto['precio']}
Cantidad: {producto['cantidad']}
-----------------------------
""")

    # ACTUALIZAR
    elif opcion == "3":

        try:

            id_producto = int(input("ID del producto: "))

            nombre = input("Nuevo nombre: ")
            descripcion = input("Nueva descripción: ")
            precio = float(input("Nuevo precio: "))
            cantidad = int(input("Nueva cantidad: "))

            spa.actualizar_producto(
                id_producto,
                nombre,
                descripcion,
                precio,
                cantidad
            )

            print("Producto actualizado correctamente")

        except ValueError as e:
            print("Error:", e)

    # ELIMINAR
    elif opcion == "4":

        try:

            id_producto = int(input("ID del producto a eliminar: "))

            spa.eliminar_producto(id_producto)

            print("Producto eliminado correctamente")

        except ValueError as e:
            print("Error:", e)

    # SALIR
    elif opcion == "5":

        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")