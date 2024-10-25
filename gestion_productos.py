import os

# Inicializar la lista de productos
productos = []

def añadir_producto():
    nombre = input("Introduce el nombre del producto: ")
    while True:
        try:
            precio = float(input("Introduce el precio del producto: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para el precio.")
    
    while True:
        try:
            cantidad = int(input("Introduce la cantidad disponible: "))
            break
        except ValueError:
            print("Por favor, introduce un número válido para la cantidad.")

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(producto)
    print(f"Producto '{nombre}' añadido exitosamente.")

def ver_productos():
    if not productos:
        print("No hay productos en la lista.")
        return
    
    print("\nLista de productos:")
    for producto in productos:
        print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    print()

def actualizar_producto():
    nombre = input("Introduce el nombre del producto a actualizar: ")
    for producto in productos:
        if producto['nombre'].lower() == nombre.lower():
            nuevo_nombre = input("Introduce el nuevo nombre (deja en blanco para no cambiar): ")
            nuevo_precio = input("Introduce el nuevo precio (deja en blanco para no cambiar): ")
            nueva_cantidad = input("Introduce la nueva cantidad (deja en blanco para no cambiar): ")

            if nuevo_nombre:
                producto['nombre'] = nuevo_nombre
            if nuevo_precio:
                try:
                    producto['precio'] = float(nuevo_precio)
                except ValueError:
                    print("Precio no válido. No se actualizará.")
            if nueva_cantidad:
                try:
                    producto['cantidad'] = int(nueva_cantidad)
                except ValueError:
                    print("Cantidad no válida. No se actualizará.")
                
            print(f"Producto '{nombre}' actualizado exitosamente.")
            return
    print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto():
    nombre = input("Introduce el nombre del producto a eliminar: ")
    global productos
    productos = [producto for producto in productos if producto['nombre'].lower() != nombre.lower()]
    print(f"Producto '{nombre}' eliminado exitosamente.")

def guardar_datos():
    with open("productos.txt", "w") as file:
        for producto in productos:
            file.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")
    print("Datos guardados exitosamente en 'productos.txt'.")

def cargar_datos():
    if os.path.exists("productos.txt"):
        with open("productos.txt", "r") as file:
            for line in file:
                nombre, precio, cantidad = line.strip().split(',')
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        print("Datos cargados exitosamente desde 'productos.txt'.")
    else:
        print("No se encontró el archivo 'productos.txt'.")

def menu():
    cargar_datos()
    while True:
        print("\n1: Añadir producto")
        print("2: Ver productos")
        print("3: Actualizar producto")
        print("4: Eliminar producto")
        print("5: Guardar datos y salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            añadir_producto()
        elif opcion == '2':
            ver_productos()
        elif opcion == '3':
            actualizar_producto()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            guardar_datos()
            break
        else:
            print("Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    menu()
