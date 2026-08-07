# === METADATA ===
# title: Gestión de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con los nombres de los primeros N productos más caros que cumplan con la condición de stock.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar listas por comprensión o la función filter para descartar el stock en cero, la función sorted con una función lambda para ordenar, y rebanado (slicing) para limitar la cantidad.

# === SOLUTION ===
def procesar_inventario(productos, limite):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'], reverse=True)
    nombres = [p['nombre'] for p in productos_ordenados[:limite]]
    return nombres

# === TESTS ===
try:
    inv = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 2}
    ]
    assert procesar_inventario(inv, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 1) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")