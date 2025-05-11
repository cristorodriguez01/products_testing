from products import Producto, Inventario
import pytest

def test_crear_producto_valido():
    producto = Producto("001", "Laptop", 1200.50, 10)
    assert producto.codigo == "001"
    assert producto.nombre == "Laptop"
    assert producto.precio == 1200.50
    assert producto.existencias == 10

def test_producto_precio_negativo():
    with pytest.raises(ValueError):
        Producto("001", "Laptop", -100, 10)
