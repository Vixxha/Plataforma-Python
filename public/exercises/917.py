# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a 0, ordenarlos de forma ascendente según su 'precio' y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una función `lambda` para ordenar por precio, y otra comprensión de listas para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Lapicero', 'precio': 1.20, 'stock': 100},
        {'nombre': 'Borrador', 'precio': 0.50, 'stock': 0},
        {'nombre': 'Cuaderno', 'precio': 3.50, 'stock': 12}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Agotado', 'precio': 10.0, 'stock': 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'B', 'precio': 10.0, 'stock': 2},
        {'nombre': 'A', 'precio': 5.0, 'stock': 5}
    ]
    assert procesar_inventario(inv3) == ['A', 'B'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")