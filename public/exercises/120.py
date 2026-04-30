# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente busque el nombre del producto más barato de esa lista filtrada. Si la lista está vacía, devuelve None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Primero usa una lista por comprensión para filtrar, luego el método .sort() o sorted() con una llave lambda, y finalmente accede al primer elemento.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    if not disponibles:
        return None
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 25, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 0},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == 'Cable', "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'A', 'precio': 100, 'stock': 0}]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")