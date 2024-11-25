class Producto:
    def __init__(self, nombre="Desconocido", categoria="General", precio=1.0, cantidad=0):
        self.__nombre = nombre.upper()
        self.__categoria = categoria.upper()
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
  
    def get_nombre(self):
        return self.__nombre
 
    def get_categoria(self):
        return self.__categoria
 
    def get_precio(self):
        return self.__precio
  
    def get_cantidad(self):
        return self.__cantidad

    # Setters
    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
        self.__precio = precio

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        self.__cantidad = cantidad

    def __str__(self):
        return f"Producto(nombre:{self.__nombre}, categoría:{self.__categoria}, precio:{self.__precio:.2f}, cantidad:{self.__cantidad})"


class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            raise ValueError("El producto ya existe en el inventario.")
        self.__productos.append(producto)

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                return
        raise ValueError("Producto no encontrado.")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                return
        raise ValueError("Producto no encontrado.")

    def mostrar_inventario(self):
        if not self.__productos:
            print(f"{self.colored_text('=== Estado Actual del Inventario ===', 'cyan')}")
            print(f"{self.colored_text('El inventario está vacío.', 'red')}")
        else:
            print(f"{self.colored_text('=== Estado Actual del Inventario ===', 'cyan')}")
            for producto in self.__productos:
                print(producto)

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        raise ValueError("Producto no encontrado.")

    @staticmethod
    def colored_text(text, color):
        colors = {
            "red": "\033[91m",
            "green": "\033[92m",
            "yellow": "\033[93m",
            "blue": "\033[94m",
            "magenta": "\033[95m",
            "cyan": "\033[96m",
            "white": "\033[97m",
            "reset": "\033[0m"
        }
        return f"{colors[color]}{text}{colors['reset']}"


def menu():
    inventario = Inventario()

    while True:
        print("\n=== Menú de Inventario ===")
        print(inventario.colored_text("1. Agregar producto", "green"))
        print(inventario.colored_text("2. Actualizar producto", "yellow"))
        print(inventario.colored_text("3. Eliminar producto", "magenta"))
        print(inventario.colored_text("4. Mostrar inventario", "cyan"))
        print(inventario.colored_text("5. Buscar producto", "blue"))
        print(inventario.colored_text("6. Salir", "red"))

        opcion = input("Seleccione una opción (1-6): ")

        if opcion == '1':
            while True:
                nombre = input("Ingrese el nombre del producto (no puede estar vacío): ")
                if nombre.strip():  # Verifica que no esté vacío
                    break
                else:
                    print(inventario.colored_text("El nombre no puede estar vacío. Intente de nuevo.", "red"))

            while True:
                categoria = input("Ingrese la categoría del producto (no puede estar vacío): ")
                if categoria.strip():  # Verifica que no esté vacío
                    break
                else:
                    print(inventario.colored_text("La categoría no puede estar vacía. Intente de nuevo.", "red"))

            precio = input("Ingrese el precio del producto (deje en blanco para usar 1.0): ")
            cantidad = input("Ingrese la cantidad en stock (deje en blanco para usar 0): ")

            precio = float(precio) if precio else 1.0
            cantidad = int(cantidad) if cantidad else 0
            
            try:
                inventario.agregar_producto(Producto(nombre, categoria, precio, cantidad))
                print(inventario.colored_text("Producto agregado exitosamente.", "green"))
            except ValueError as e:
                print(inventario.colored_text(str(e), "red"))

        elif opcion == '2':
            while True:
                nombre = input("Ingrese el nombre del producto a actualizar (no puede estar vacío) : ").upper()
                if nombre.strip():  # Verifica que no esté vacío
                    break
                else:
                    print(inventario.colored_text("El nombre no puede estar vacío. Intente de nuevo.", "red"))

            nuevo_precio = input("Ingrese el nuevo precio (deje en blanco si no desea cambiarlo): ")
            nueva_cantidad = input("Ingrese la nueva cantidad (deje en blanco si no desea cambiarlo): ")

            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            
            try:
                inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)
                print(inventario.colored_text("Producto actualizado exitosamente.", "green"))
            except ValueError as e:
                print(inventario.colored_text(str(e), "red"))

        elif opcion == '3':
            nombre = input("Ingrese el nombre del producto a eliminar: ").upper()
            try:
                inventario.eliminar_producto(nombre)
                print(inventario.colored_text(f"Producto: '{nombre}' eliminado exitosamente.", "green"))
            except ValueError as e:
                print(inventario.colored_text(str(e), "red"))

        elif opcion == '4':
            inventario.mostrar_inventario()

        elif opcion == '5':
            nombre = input("Ingrese el nombre del producto a buscar: ").upper()
            try:
                producto_encontrado = inventario.buscar_producto(nombre)
                print(inventario.colored_text("Producto encontrado:", "green"), producto_encontrado)
            except ValueError as e:
                print(inventario.colored_text(str(e), "red"))

        elif opcion == '6':
            print(inventario.colored_text("Saliendo del programa...", "yellow"))
            break

        else:
            print(inventario.colored_text("Opción inválida. Por favor, seleccione una opción válida.", "red"))


# Ejecución del programa
if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nSaliendo del programa por interrupción del usuario. ¡Adiós!")
