# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar listas por comprensión o la función filter para los filtros, sorted con una función anónima (lambda) para ordenar por precio, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 40, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Mouse', 'Audífonos', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 1},
        {'nombre': 'USB', 'precio': 10, 'stock': 5}
    ]
    assert procesar_inventario(inv2) == ['USB', 'Laptop'], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Agotado', 'precio': 5, 'stock': 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")