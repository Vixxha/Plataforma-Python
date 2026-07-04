# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos encontrados.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Utiliza una lista de comprensión para filtrar el stock, luego emplea el método sort() o la función sorted() con una expresión lambda como clave de ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtramos productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenamos por precio
    disponibles.sort(key=lambda x: x['precio'])
    # Extraemos solo los nombres
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 2}
    ]
    # Teclado no debe aparecer por stock 0. Orden: Mouse(20), Webcam(80), Monitor(200)
    assert procesar_inventario(inventario) == ['Mouse', 'Webcam', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: el caso base de stock cero falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")