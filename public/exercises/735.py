# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos encontrados que cuesten menos de 500.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero filtra con una comprensión de lista, luego usa el método sort() o la función sorted() con una llave lambda, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0 y precio < 500
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] < 500]
    # Ordenar por precio de menor a mayor
    filtrados.sort(key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 800, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 150, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 300, 'stock': 0}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 1000, 'stock': 1}]) == [], "Error: no debe incluir productos caros."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")