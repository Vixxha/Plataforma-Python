# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y finalmente busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa un filtro (o comprensión de lista) para eliminar productos sin stock, el método .sort() con una lambda para el precio y accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    if not disponibles:
        return None
    disponibles.sort(key=lambda x: x['precio'])
    return disponibles[0]['nombre']

# === TESTS ===
try:
    inventario1 = [
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 15, 'stock': 5},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 0}
    ]
    inventario2 = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 2},
        {'nombre': 'Tablet', 'precio': 300, 'stock': 5}
    ]
    assert procesar_inventario(inventario1) == 'Teclado', "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario2) == 'Tablet', "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")