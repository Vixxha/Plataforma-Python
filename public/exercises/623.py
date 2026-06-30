# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve los nombres de aquellos cuyo precio sea menor a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa una lista de comprensión o filter() para el stock, el método .sort() o sorted() con una llave lambda para el precio, y finalmente otra iteración para el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados if p['precio'] < presupuesto]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert procesar_inventario(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")