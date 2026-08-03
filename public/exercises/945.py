# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función filter() o una comprensión de lista para filtrar, el método .sort() o la función sorted() con una función lambda para ordenar, y otra comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.5, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 12.0, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 1.5, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.5, 'stock': 25}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Tablet', 'precio': 300.0, 'stock': 0},
        {'nombre': 'Cable', 'precio': 15.0, 'stock': 2}
    ]
    assert procesar_inventario(inv2) == ['Cable'], "Error: considera casos límites en tu lógica."
    
    assert procesar_inventario([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")