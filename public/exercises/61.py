# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Utiliza una lista de comprensión (list comprehension) para filtrar, el método .sort() o la función sorted() con una llave lambda para ordenar, y finalmente recorre la lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] < 5]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 1},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 3},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 10}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: debería devolver lista vacía si no hay stock bajo."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}, {'nombre': 'A', 'precio': 1, 'stock': 2}]) == ['A', 'B'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")