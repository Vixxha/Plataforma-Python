# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea menor a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero usa una lista por comprensión para filtrar, luego el método .sort() o sorted() con una función lambda, y finalmente realiza una búsqueda/filtro por precio.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles if p['precio'] < presupuesto]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert procesar_inventario(inventario, 60) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")