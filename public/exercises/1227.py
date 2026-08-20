# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente devuelva una lista con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función `filter` o una comprensión de lista para filtrar, y la función `sorted` pasando una función lambda como argumento `key` para manejar criterios múltiples de ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 3.50, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 0.50, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 1.20, 'stock': 25}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Z', 'precio': 10.0, 'stock': 2},
        {'nombre': 'A', 'precio': 10.0, 'stock': 5}
    ]
    assert procesar_inventario(inv2) == ['A', 'Z'], "Error: considera casos límites en tu lógica (empates en precio)."
    
    inv3 = [
        {'nombre': 'Tablet', 'precio': 300.0, 'stock': 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló (inventario sin stock)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")