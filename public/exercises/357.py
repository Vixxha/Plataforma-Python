# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Usa una lista de comprensión para el filtro, la función sorted() con una llave lambda para el ordenamiento y finalmente una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['stock'] < 5]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 3},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 1}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el filtro no excluyó productos con stock suficiente."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")