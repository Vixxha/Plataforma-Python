# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Utiliza el método filter() o una comprensión de listas para filtrar, la función sorted() con una llave lambda para ordenar, y accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio de menor a mayor
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # Retornar el nombre del más barato si existe, sino None
    return ordenados[0]['nombre'] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 25, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 0},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == 'Cable', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 100, 'stock': 0}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 10, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")