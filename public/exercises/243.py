# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dada una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de forma descendente y busca si existe un producto específico por nombre. La función debe retornar una lista con los nombres de los productos filtrados y ordenados, y un booleano indicando si el producto buscado está en la lista original.
# difficulty: Intermedio
# expected_output: (['Laptop', 'Monitor'], True)
# hint: Utiliza la función filter() o una comprensión de listas para filtrar, sorted() con el argumento key para ordenar, y el operador 'in' para buscar.

# === SOLUTION ===
def gestionar_inventario(productos, nombre_buscado):
    filtrados = [p for p in productos if p['stock'] < 5]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    nombres_ordenados = [p['nombre'] for p in ordenados]
    existe = any(p['nombre'] == nombre_buscado for p in productos)
    return (nombres_ordenados, existe)

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 3},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 8}
    ]
    assert gestionar_inventario(inventario, 'Mouse') == (['Laptop', 'Monitor'], True), "Error: el test 1 ha fallado."
    assert gestionar_inventario(inventario, 'Tablet') == (['Laptop', 'Monitor'], False), "Error: considera casos donde el producto no existe."
    assert gestionar_inventario([], 'Nada') == ([], False), "Error: el caso de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")