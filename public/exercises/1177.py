# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos ordenados que cumplan con la condición.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una función `lambda` para ordenar por el precio, y otra comprensión de listas para extraer los nombres.

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
    # Stock > 0: Monitor (200), Mouse (25), Audífonos (40)
    # Ordenados por precio: Mouse (25), Audífonos (40), Monitor (200)
    assert procesar_inventario(inv1) == ['Mouse', 'Audífonos', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 0},
        {'nombre': 'USB', 'precio': 10, 'stock': 50}
    ]
    assert procesar_inventario(inv2) == ['USB'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")