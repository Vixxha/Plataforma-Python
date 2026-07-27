# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos ordenados que cumplan con la condición.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para la condición, la función sorted() con una función lambda para ordenar, y otra comprensión para extraer solo los nombres.

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
        {'nombre': 'Audífonos', 'precio': 50, 'stock': 2}
    ]
    # 'Teclado' tiene stock 0, se excluye. 
    # Orden por precio: Mouse (25), Audífonos (50), Monitor (200). 
    # Nota: Si el precio es igual, el orden original se mantiene estable en Python.
    assert procesar_inventario(inv1) == ['Mouse', 'Audífonos', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 0},
        {'nombre': 'USB', 'precio': 10, 'stock': 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Libreta', 'precio': 5, 'stock': 100}
    ]
    assert procesar_inventario(inv3) == ['Libreta'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")