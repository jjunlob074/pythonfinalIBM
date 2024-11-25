from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Lógica de inventario
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
        try:
            precio = float(precio)  # Intenta convertir a float
        except ValueError:
            raise ValueError("El precio debe ser un número válido.")
    
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que 0.")
    
        self.__precio = precio

    def set_cantidad(self, cantidad):
        try:
            cantidad = int(cantidad)  # Intenta convertir a int
        except ValueError:
            raise ValueError("La cantidad debe ser un número entero válido.")
        
        if cantidad < 0:
            raise ValueError("La cantidad debe ser mayor o igual que 0.")
        
        self.__cantidad = cantidad


    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "categoria": self.__categoria,
            "precio": self.__precio,
            "cantidad": self.__cantidad
        }

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
                # Actualizar precio si se proporciona, si no, mantener el actual
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                # Actualizar cantidad si se proporciona, si no, mantener la actual
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
        return [p.to_dict() for p in self.__productos]

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                return producto
        raise ValueError("Producto no encontrado.")

# Crear un objeto de inventario global
inventario = Inventario()

# Rutas de API
@app.route('/api/productos', methods=['GET'])
def obtener_productos():
    productos = inventario.mostrar_inventario()
    return jsonify(productos)

@app.route('/api/producto', methods=['POST'])
def agregar_producto():
    data = request.json
    nombre = data.get('nombre').upper()
    categoria = data.get('categoria').upper()
    precio = float(data.get('precio'))
    cantidad = int(data.get('cantidad'))

    try:
        nuevo_producto = Producto(nombre, categoria, precio, cantidad)
        inventario.agregar_producto(nuevo_producto)
        return jsonify({"message": "Producto agregado exitosamente."}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/producto/<nombre>', methods=['PUT'])
def actualizar_producto(nombre):
    data = request.json
    nuevo_precio = data.get('precio')
    nueva_cantidad = data.get('cantidad')

    try:
        # Comprobar y convertir el nuevo precio a float
        if nuevo_precio is not None and nuevo_precio != "":
            try:
                nuevo_precio = float(nuevo_precio)
                # Verificar si el precio es mayor que 0
                if nuevo_precio <= 0:  
                    raise ValueError("El precio debe ser mayor que 0.")
            except ValueError:
                raise ValueError("El precio debe ser un número válido (distinto de 0).")  # Mensaje si no es un número
        else:
            nuevo_precio = None  # Asignar None si no se proporciona un nuevo precio

        # Comprobar y convertir la nueva cantidad a int
        if nueva_cantidad is not None and nueva_cantidad != "":
            try:
                nueva_cantidad = int(nueva_cantidad)
                # Verificar si la cantidad es mayor o igual que 0
                if nueva_cantidad < 0:  
                    raise ValueError("La cantidad debe ser mayor o igual que 0.")
            except ValueError:
                raise ValueError("La cantidad debe ser un número entero válido.")  # Mensaje si no es un número
        else:
            nueva_cantidad = None  # Asignar None si no se proporciona una nueva cantidad

        # Llamar al método actualizar con los valores proporcionados
        inventario.actualizar_producto(nombre.upper(), nuevo_precio, nueva_cantidad)
        return jsonify({"message": "Producto actualizado exitosamente."})

    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@app.route('/api/producto/<nombre>', methods=['DELETE'])
def eliminar_producto(nombre):
    try:
        inventario.eliminar_producto(nombre.upper())
        return jsonify({"message": f"Producto '{nombre}' eliminado exitosamente."})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

@app.route('/api/producto/<nombre>', methods=['GET'])
def buscar_producto(nombre):
    try:
        producto = inventario.buscar_producto(nombre.upper())
        return jsonify(producto.to_dict())
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

# Ruta para servir el HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=False)

