# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y devuelva solo los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Utiliza una lista de comprensión o filter() para el stock, el método sort() o la función sorted() con una clave lambda para el precio, y finalmente una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 30, 'stock': 2}
    ]
    # Filtra stock > 0: Monitor (200), Mouse (20), Auriculares (30)
    # Ordena por precio: Mouse (20), Auriculares (30), Monitor (200)
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: El orden o filtro es incorrecto."
    assert procesar_inventario([]) == [], "Error: El caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: El filtro de stock no eliminó el producto agotado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")