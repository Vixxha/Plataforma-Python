# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Usa un filtro (o list comprehension), el método .sort() o la función sorted() con un parámetro 'key', y finalmente una lista por comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio de menor a mayor
    filtrados.sort(key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 1},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 3},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 10}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == ['A'], "Error: el caso de un solo elemento falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el caso con stock suficiente debería devolver lista vacía."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")