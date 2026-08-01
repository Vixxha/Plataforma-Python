# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función filter() o list comprehensions para filtrar, sorted() con una función lambda para ordenar por precio, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p.get('stock', 0) > 0]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 5},
        {'nombre': 'Borrador', 'precio': 1.0, 'stock': 0},
        {'nombre': 'Cuaderno', 'precio': 15.5, 'stock': 12},
        {'nombre': 'Lapicero', 'precio': 2.5, 'stock': 50}
    ]
    assert procesar_inventario(inventario_1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'Tablet', 'precio': 300.0, 'stock': 0},
        {'nombre': 'Cable', 'precio': 10.0, 'stock': 2}
    ]
    assert procesar_inventario(inventario_2) == ['Cable'], "Error: considera casos límites en tu lógica."
    
    inventario_3 = []
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")