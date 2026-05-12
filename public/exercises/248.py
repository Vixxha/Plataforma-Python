# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente busque el nombre del producto más barato de esa lista filtrada.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa una comprensión de listas para filtrar, la función 'sorted' con un parámetro 'key' para ordenar y el índice para acceder al elemento.

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
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 15, 'stock': 5},
        {'nombre': 'Webcam', 'precio': 40, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")