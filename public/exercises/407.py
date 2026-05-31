# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y devuelva solo los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Utiliza una lista de comprensión o la función filter() para el stock, y sorted() con un parámetro key tipo lambda para ordenar por precio.

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
    # Filtra (quita Teclado por stock 0), ordena por precio: Mouse(20), Auriculares(30), Monitor(200)
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'PC', 'precio': 1000, 'stock': 0}]) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")