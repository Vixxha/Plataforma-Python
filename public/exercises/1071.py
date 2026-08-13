# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a 0, ordenarlos de forma ascendente según su 'precio' y, finalmente, retornar una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzanas', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento por precio, y otra comprensión de listas para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Leche', 'precio': 2.0, 'stock': 5},
        {'nombre': 'Huevos', 'precio': 3.0, 'stock': 0},
        {'nombre': 'Manzanas', 'precio': 1.0, 'stock': 20}
    ]
    assert procesar_inventario(inv1) == ['Manzanas', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1000.0, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 5}
    ]
    assert procesar_inventario(inv2) == ['Teclado', 'Laptop'], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Agotado', 'precio': 10.0, 'stock': 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")