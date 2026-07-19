# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos encontrados.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Usa un filtro para descartar productos sin stock, luego el método 'sort' o 'sorted' con una función lambda como clave.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 30, 'stock': 2}
    ]
    # Filtra (quita Teclado), ordena (Mouse:20, Auriculares:30, Monitor:200)
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: considera el filtro de stock."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")