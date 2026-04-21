# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de forma descendente y devuelve el nombre del primer producto resultante. Si no hay productos con bajo stock, retorna None.
# difficulty: Intermedio
# expected_output: 'Teclado Mecánico'
# hint: Usa una lista de comprensión o filter() para el criterio de stock, el método .sort() o sorted() con una lambda para el ordenamiento, y asegúrate de manejar listas vacías.

# === SOLUTION ===
def procesar_inventario(productos):
    bajo_stock = [p for p in productos if p['stock'] < 5]
    if not bajo_stock:
        return None
    bajo_stock.sort(key=lambda x: x['precio'], reverse=True)
    return bajo_stock[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 3},
        {'nombre': 'Teclado Mecánico', 'precio': 150, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 1}
    ]
    assert procesar_inventario(inventario) == 'Teclado Mecánico', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 20}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 50, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")