class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
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
        return f"Producto(nombre:'{self.__nombre}', categoría:'{self.__categoria}', precio:{self.__precio:.2f}, cantidad:{self.__cantidad})"


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


# Ejecución automática del programa
if __name__ == "__main__":
    inventario = Inventario()

    print(inventario.colored_text("=== Inicio del Programa ===", "green"))

    # Agregar productos
    print(inventario.colored_text("Agregando productos al inventario...", "yellow"))
    try:
        producto1 = Producto("Laptop", "Electrónica", 1200.00, 5)
        inventario.agregar_producto(producto1)
        print(inventario.colored_text(f"¡Producto '{producto1.get_nombre()}' agregado exitosamente!", "magenta"))

        producto2 = Producto("Teléfono", "Electrónica", 800.00, 10)
        inventario.agregar_producto(producto2)
        print(inventario.colored_text(f"¡Producto '{producto2.get_nombre()}' agregado exitosamente!", "magenta"))

        producto3 = Producto("Mesa", "Muebles", 150.00, 20)
        inventario.agregar_producto(producto3)
        print(inventario.colored_text(f"¡Producto '{producto3.get_nombre()}' agregado exitosamente!", "magenta"))

    except ValueError as e:
        print(inventario.colored_text(str(e), "red"))

    # Mostrar inventario al inicio
    inventario.mostrar_inventario()

    # Actualizar producto
    print("\nActualizando el producto 'Laptop'...")
    try:
        nuevo_precio = 1100.00
        nueva_cantidad = 3
        inventario.actualizar_producto("Laptop", nuevo_precio=nuevo_precio, nueva_cantidad=nueva_cantidad)
        print(inventario.colored_text("Producto 'Laptop' actualizado exitosamente.", "green"))
        print(inventario.colored_text(f"Nueva información - Precio: {nuevo_precio:.2f}, Cantidad: {nueva_cantidad}", "cyan"))
    except ValueError as e:
        print(inventario.colored_text(str(e), "red"))

    # Buscar un producto
    print("\nBuscando el producto 'Teléfono'...")
    try:
        producto_encontrado = inventario.buscar_producto("Teléfono")
        print(inventario.colored_text("Producto encontrado:", "green"), producto_encontrado)
    except ValueError as e:
        print(inventario.colored_text(str(e), "red"))

    # Eliminar un producto
    print("\nEliminando el producto 'Mesa'...")
    try:
        inventario.eliminar_producto("Mesa")
        print(inventario.colored_text("Producto 'Mesa' eliminado exitosamente.", "green"))
    except ValueError as e:
        print(inventario.colored_text(str(e), "red"))

    # Mostrar inventario al final
    inventario.mostrar_inventario()

    print(inventario.colored_text("=== Fin del Programa ===", "red"))

