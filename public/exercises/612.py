# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de forma ascendente y retorna solo los nombres de aquellos cuyo precio sea superior a 100.
# difficulty: Intermedio
# expected_output: ['Teclado Mecánico', 'Monitor 4K']
# hint: Primero filtra por stock, luego ordena la lista resultante y finalmente usa una comprensión de listas o un bucle para extraer los nombres cumpliendo la condición de precio.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] < 5]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados if p['precio'] > 100]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 50, 'stock': 2},
        {'nombre': 'Monitor 4K', 'precio': 300, 'stock': 1},
        {'nombre': 'Teclado Mecánico', 'precio': 120, 'stock': 3},
        {'nombre': 'Cable USB', 'precio': 10, 'stock': 10}
    ]
    assert procesar_inventario(inventario) == ['Teclado Mecánico', 'Monitor 4K'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'Barato', 'precio': 50, 'stock': 1}]) == [], "Error: el caso sin productos caros falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")