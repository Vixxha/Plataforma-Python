# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y finalmente una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio (ascendente)
    filtrados.sort(key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 1},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 4},
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 10}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: debería filtrar todos los elementos."
    assert procesar_inventario([]) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")