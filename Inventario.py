class Producto:
    def __init__(self, nombre, categoria, precio, cantidad):
        self.__nombre = nombre
        self.__categoria = categoria
        self.set_precio(precio)
        self.set_cantidad(cantidad)

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_categoria(self):
        return self.__categoria

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    # Setters con validaciones
    def set_precio(self, precio):
        if precio > 0:
            self.__precio = precio
        else:
            raise ValueError("El precio debe ser mayor que 0")

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.__cantidad = cantidad
        else:
            raise ValueError("La cantidad debe ser mayor o igual que 0")

    def __str__(self):
        return f"Producto: {self.__nombre}, Categoría: {self.__categoria}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"

class Inventario:
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        if not any(p.get_nombre() == producto.get_nombre() for p in self.__productos):
            self.__productos.append(producto)
            print(f"Producto '{producto.get_nombre()}' agregado exitosamente.")
        else:
            print(f"El producto '{producto.get_nombre()}' ya existe en el inventario.")

    def actualizar_producto(self, nombre, nuevo_precio=None, nueva_cantidad=None):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                if nuevo_precio is not None:
                    producto.set_precio(nuevo_precio)
                if nueva_cantidad is not None:
                    producto.set_cantidad(nueva_cantidad)
                print(f"Producto '{nombre}' actualizado.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def eliminar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                self.__productos.remove(producto)
                print(f"Producto '{nombre}' eliminado del inventario.")
                return
        print(f"Producto '{nombre}' no encontrado en el inventario.")

    def mostrar_inventario(self):
        if self.__productos:
            for producto in self.__productos:
                print(producto)
        else:
            print("El inventario está vacío.")

    def buscar_producto(self, nombre):
        for producto in self.__productos:
            if producto.get_nombre() == nombre:
                print("Producto encontrado:", producto)
                return producto
        print(f"Producto '{nombre}' no encontrado.")
        return None
