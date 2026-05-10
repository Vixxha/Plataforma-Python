# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de forma ascendente y devuelve únicamente una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa una lista de comprensión o filter() para filtrar, luego el método .sort() o la función sorted() con una expresión lambda para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] < 5]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    data = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 3}
    ]
    assert procesar_inventario(data) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: debería devolver lista vacía si no hay stock bajo."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}, {'nombre': 'A', 'precio': 1, 'stock': 1}]) == ['A', 'B'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")