# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los resultados por precio de forma descendente y devuelve los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Tablet', 'Monitor']
# hint: Utiliza una lista de comprensión o filter() para la condición, el método .sort() o sorted() con una función lambda para el ordenamiento y una lista de comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio de forma descendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 3},
        {'nombre': 'Tablet', 'precio': 500, 'stock': 1}
    ]
    assert procesar_inventario(inventario) == ['Tablet', 'Monitor', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'Teclado', 'precio': 50, 'stock': 10}]) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")