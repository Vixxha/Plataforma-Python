# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra aquellos que cuestan 50 o más, ordénalos de menor a mayor precio y busca el nombre del primer producto resultante que coincida con un criterio de búsqueda.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa una lista de comprensión para el filtro, el método .sort() o sorted() para ordenar y un bucle o condicional para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    if not ordenados:
        return None
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 50},
        {'nombre': 'Cable', 'precio': 10}
    ]
    assert procesar_inventario(inventario, 50) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 200) == None, "Error: debería devolver None si no hay coincidencias."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}], 5) == "A", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")