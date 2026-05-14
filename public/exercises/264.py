# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Usa una lista de comprensión para filtrar, el método sort() o la función sorted() con una clave lambda para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio ascendente
    filtrados.sort(key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 4},
        {'nombre': 'Teclado', 'precio': 20, 'stock': 1},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 10}
    ]
    resultado_esperado = ['Teclado', 'Mouse', 'Monitor']
    assert procesar_inventario(inventario) == resultado_esperado, "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50, 'stock': 0}]) == ['B'], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")