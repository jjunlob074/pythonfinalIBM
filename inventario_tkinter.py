import tkinter as tk
from tkinter import ttk, messagebox

# Clase Producto e Inventario tal como la tienes
class Producto:
    def __init__(self, nombre="Desconocido", categoria="General", precio=1.0, cantidad=0):
        self.__nombre = nombre.upper()
        self.__categoria = categoria.upper()
        self.__precio = precio
        self.__cantidad = cantidad

    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

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
        return self.__productos

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        raise ValueError("Producto no encontrado.")

# Interfaz gráfica mejorada con pestañas y un diseño profesional
class InventarioApp:
    def __init__(self, root):
        self.inventario = Inventario()

        # Configurar ventana principal
        root.title("Sistema de Gestión de Inventario")
        root.geometry("720x280")
        root.resizable(False, False)

        # Crear un notebook para las pestañas
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True)

        # Pestaña 1: Agregar Producto
        self.tab_agregar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_agregar, text="Agregar Producto")

        # Pestaña 2: Actualizar Producto
        self.tab_actualizar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_actualizar, text="Actualizar Producto")

        # Pestaña 3: Eliminar Producto
        self.tab_eliminar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_eliminar, text="Eliminar Producto")

        # Pestaña 4: Mostrar Inventario
        self.tab_mostrar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_mostrar, text="Mostrar Inventario")

        # Pestaña 5: Buscar Producto
        self.tab_buscar = ttk.Frame(self.notebook)
        self.notebook.add(self.tab_buscar, text="Buscar Producto")

        # Configurar cada pestaña
        self.config_tab_agregar()
        self.config_tab_actualizar()
        self.config_tab_eliminar()
        self.config_tab_mostrar()
        self.config_tab_buscar()

        # Mostrar inventario automáticamente al inicio
        self.mostrar_inventario()

    def config_tab_agregar(self):
        # Widgets para agregar productos
        ttk.Label(self.tab_agregar, text="Nombre del Producto").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre = ttk.Entry(self.tab_agregar)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre.bind("<FocusOut>", self.convertir_mayusculas)

        ttk.Label(self.tab_agregar, text="Categoría").grid(row=1, column=0, padx=10, pady=10)
        self.entry_categoria = ttk.Entry(self.tab_agregar)
        self.entry_categoria.grid(row=1, column=1, padx=10, pady=10)
        self.entry_categoria.bind("<FocusOut>", self.convertir_mayusculas)

        ttk.Label(self.tab_agregar, text="Precio").grid(row=2, column=0, padx=10, pady=10)
        self.entry_precio = ttk.Entry(self.tab_agregar)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10)

        ttk.Label(self.tab_agregar, text="Cantidad").grid(row=3, column=0, padx=10, pady=10)
        self.entry_cantidad = ttk.Entry(self.tab_agregar)
        self.entry_cantidad.grid(row=3, column=1, padx=10, pady=10)

        ttk.Button(self.tab_agregar, text="Agregar Producto", command=self.agregar_producto).grid(row=4, column=0, columnspan=2, padx=10, pady=20)

    def config_tab_actualizar(self):
        # Widgets para actualizar productos
        ttk.Label(self.tab_actualizar, text="Nombre del Producto a Actualizar").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_actualizar = ttk.Entry(self.tab_actualizar)
        self.entry_nombre_actualizar.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre_actualizar.bind("<FocusOut>", self.convertir_mayusculas)

        ttk.Label(self.tab_actualizar, text="Nuevo Precio").grid(row=1, column=0, padx=10, pady=10)
        self.entry_nuevo_precio = ttk.Entry(self.tab_actualizar)
        self.entry_nuevo_precio.grid(row=1, column=1, padx=10, pady=10)

        ttk.Label(self.tab_actualizar, text="Nueva Cantidad").grid(row=2, column=0, padx=10, pady=10)
        self.entry_nueva_cantidad = ttk.Entry(self.tab_actualizar)
        self.entry_nueva_cantidad.grid(row=2, column=1, padx=10, pady=10)

        ttk.Button(self.tab_actualizar, text="Actualizar Producto", command=self.actualizar_producto).grid(row=3, column=0, columnspan=2, padx=10, pady=20)

    def config_tab_eliminar(self):
        # Widgets para eliminar productos
        ttk.Label(self.tab_eliminar, text="Nombre del Producto a Eliminar").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_eliminar = ttk.Entry(self.tab_eliminar)
        self.entry_nombre_eliminar.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre_eliminar.bind("<FocusOut>", self.convertir_mayusculas)

        ttk.Button(self.tab_eliminar, text="Eliminar Producto", command=self.eliminar_producto).grid(row=1, column=0, columnspan=2, padx=10, pady=20)

    def config_tab_mostrar(self):
        # Widgets para mostrar inventario
        self.listbox_inventario = tk.Listbox(self.tab_mostrar)
        self.listbox_inventario.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def config_tab_buscar(self):
        # Widgets para buscar productos
        ttk.Label(self.tab_buscar, text="Nombre del Producto a Buscar").grid(row=0, column=0, padx=10, pady=10)
        self.entry_nombre_buscar = ttk.Entry(self.tab_buscar)
        self.entry_nombre_buscar.grid(row=0, column=1, padx=10, pady=10)
        self.entry_nombre_buscar.bind("<FocusOut>", self.convertir_mayusculas)

        ttk.Button(self.tab_buscar, text="Buscar Producto", command=self.buscar_producto).grid(row=1, column=0, columnspan=2, padx=10, pady=20)

        self.label_resultado_buscar = ttk.Label(self.tab_buscar, text="")
        self.label_resultado_buscar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Funciones de interacción con el inventario
    def agregar_producto(self):
        nombre = self.entry_nombre.get().strip()
        categoria = self.entry_categoria.get().strip()
        precio = self.entry_precio.get().strip()
        cantidad = self.entry_cantidad.get().strip()

        if not nombre or not categoria:
            messagebox.showerror("Error", "El nombre y la categoría son obligatorios.")
            return

        try:
            precio = float(precio) if precio else 1.0
            cantidad = int(cantidad) if cantidad else 0
        except ValueError:
            messagebox.showerror("Error", "Precio o cantidad inválidos.")
            return

        try:
            producto = Producto(nombre, categoria, precio, cantidad)
            self.inventario.agregar_producto(producto)
            messagebox.showinfo("Éxito", "Producto agregado exitosamente.")
            self.mostrar_inventario()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def actualizar_producto(self):
        nombre = self.entry_nombre_actualizar.get().strip()
        nuevo_precio = self.entry_nuevo_precio.get().strip()
        nueva_cantidad = self.entry_nueva_cantidad.get().strip()

        if not nombre:
            messagebox.showerror("Error", "El nombre del producto a actualizar es requerido.")
            return

        try:
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
        except ValueError:
            messagebox.showerror("Error", "Precio o cantidad inválidos.")
            return

        try:
            self.inventario.actualizar_producto(nombre, nuevo_precio, nueva_cantidad)
            messagebox.showinfo("Éxito", "Producto actualizado exitosamente.")
            self.mostrar_inventario()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def eliminar_producto(self):
        nombre = self.entry_nombre_eliminar.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto a eliminar es requerido.")
            return

        try:
            self.inventario.eliminar_producto(nombre)
            messagebox.showinfo("Éxito", "Producto eliminado exitosamente.")
            self.mostrar_inventario()
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def mostrar_inventario(self):
        self.listbox_inventario.delete(0, tk.END)
        productos = self.inventario.mostrar_inventario()
        if not productos:
            self.listbox_inventario.insert(tk.END, "El inventario está vacío.")
        else:
            for producto in productos:
                self.listbox_inventario.insert(tk.END, str(producto))

    def buscar_producto(self):
        nombre = self.entry_nombre_buscar.get().strip()
        if not nombre:
            messagebox.showerror("Error", "El nombre del producto a buscar es requerido.")
            return

        try:
            producto = self.inventario.buscar_producto(nombre)
            self.label_resultado_buscar.config(text=str(producto))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def convertir_mayusculas(self, event):
        # Convierte el texto a mayúsculas cuando el usuario cambia de campo
        current_text = event.widget.get().upper()
        event.widget.delete(0, tk.END)
        event.widget.insert(0, current_text)

if __name__ == "__main__":
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()

