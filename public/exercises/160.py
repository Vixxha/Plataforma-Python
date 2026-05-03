# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Utiliza una lista de comprensión (list comprehension) para filtrar, el método .sort() o la función sorted() con una llave lambda para ordenar, y finalmente recorre la lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio ascendente
    filtrados.sort(key=lambda x: x['precio'])
    # Retornar lista de nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 20, 'stock': 1},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 4},
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 10}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Mouse', 'Monitor'], "Error: el orden o filtrado es incorrecto."
    assert procesar_inventario([]) == [], "Error: debería manejar listas vacías."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el filtro de stock falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")