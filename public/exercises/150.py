# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato. La función debe retornar el nombre del producto más económico tras aplicar el filtro.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Primero filtra la lista usando una comprensión de lista, luego utiliza la función sorted() o el método sort() con una llave (lambda) para ordenar, y finalmente accede al primer elemento.

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
        {'nombre': 'Laptop', 'precio': 800, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 100, 'stock': 0}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50, 'stock': 1}]) == "B", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")