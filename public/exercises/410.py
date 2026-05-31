# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos que cuestan menos de 500, ordénalos de forma descendente por precio y encuentra el nombre del producto más caro resultante de esa lista filtrada.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Primero usa una lista por comprensión para filtrar, luego el método .sort() con una clave (lambda) para ordenar, y finalmente accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 500]
    if not filtrados:
        return None
    filtrados.sort(key=lambda x: x['precio'], reverse=True)
    return filtrados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 450},
        {'nombre': 'Monitor', 'precio': 300}
    ]
    assert procesar_inventario(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'Caro', 'precio': 1000}]) == None, "Error: debería devolver None si no hay elementos menores a 500."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}, {'nombre': 'B', 'precio': 20}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")