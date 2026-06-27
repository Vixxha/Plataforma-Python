# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente devuelva solo los nombres de los productos.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Usa una lista de comprensión para el filtro, el método .sort() con una función lambda para el ordenamiento y finalmente una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 30, 'stock': 2}
    ]
    # Caso: Ordenar por precio, filtrar los de stock 0
    # Teclado no debe aparecer, el orden correcto es Mouse (20), Auriculares (30), Monitor (200)
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: debería filtrar productos sin stock."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}, {'nombre': 'A', 'precio': 1, 'stock': 1}]) == ['A', 'B'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")