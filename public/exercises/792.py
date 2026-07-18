# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: {'nombre': 'Teclado', 'precio': 20}
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con el método sorted() o .sort() usando una llave lambda.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return ordenados[0] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 20, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 15, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 45, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == {'nombre': 'Teclado', 'precio': 20, 'stock': 10}, "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == {'nombre': 'A', 'precio': 10, 'stock': 1}, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50, 'stock': 0}]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")