class Venta:
    def __init__(self, codigo, cantidad=0):
        self.codigo = codigo
        self.cantidad = cantidad
        self._validar()

    def _validar(self):
        if not isinstance(self.codigo, str) or len(self.codigo) == 0:
            raise ValueError("El código debe ser una cadena no vacía")
        if not isinstance(self.cantidad, int) or self.cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo")


class Producto:
    def __init__(self, codigo, nombre, precio, existencias=0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.existencias = existencias
        self._validar()

    def _validar(self):
        if not isinstance(self.codigo, str) or len(self.codigo) == 0:
            raise ValueError("El código debe ser una cadena no vacía")

        if not isinstance(self.nombre, str) or len(self.nombre) == 0:
            raise ValueError("El nombre debe ser una cadena no vacía")

        if not isinstance(self.precio, (int, float)) or self.precio <= 0:
            raise ValueError("El precio debe ser un número positivo")

        if not isinstance(self.existencias, int) or self.existencias < 0:
            raise ValueError("Las existencias deben ser un entero no negativo")

    def reducir_existencias(self, cantidad):
        nueva_cantidad = self.existencias - cantidad
        if nueva_cantidad < 0:
            raise ValueError(f"No hay suficientes existencias. Disponible: {self.existencias}")

        self.existencias = nueva_cantidad
        return self.existencias

    def aplicar_descuento(self, porcentaje):
        if not isinstance(porcentaje, (int, float)):
            raise ValueError("El porcentaje debe ser un número")

        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje debe estar entre 0 y 100")

        factor = 1 - (porcentaje / 100)
        self.precio = round(self.precio * factor, 2)
        return self.precio


class Inventario:
    def __init__(self):
        self.productos = {}
        self.ventas = []

    def agregar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("El objeto debe ser de tipo Producto")

        if producto.codigo in self.productos:
            raise ValueError(f"Ya existe un producto con el código {producto.codigo}")

        self.productos[producto.codigo] = producto

    def obtener_producto(self, codigo):
        if codigo not in self.productos:
            raise KeyError(f"No existe un producto con el código {codigo}")

        return self.productos[codigo]

    def eliminar_producto(self, codigo):
        if codigo not in self.productos:
            raise KeyError(f"No existe un producto con el código {codigo}")

        return self.productos.pop(codigo)

    def vender_producto(self, codigo, cantidad=1):
        if not isinstance(cantidad, int) or cantidad <= 0:
            raise ValueError("La cantidad debe ser un entero positivo")

        producto = self.obtener_producto(codigo)
        producto.reducir_existencias(cantidad)
        venta = Venta(codigo, cantidad)
        self.ventas.append(venta)
        return round(cantidad * producto.precio, 2)

    def valor_total_inventario(self):
        total = 0
        for producto in self.productos.values():
            total += producto.precio * producto.existencias
        return round(total, 2)

    def productos_agotados(self):
        return [p.codigo for p in self.productos.values() if p.existencias == 0]

    def buscar_productos(self, texto):
        if not isinstance(texto, str):
            raise ValueError("El texto de búsqueda debe ser una cadena")

        texto = texto.lower()
        return [p for p in self.productos.values() if texto in p.nombre.lower()]
