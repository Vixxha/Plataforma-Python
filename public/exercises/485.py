# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre aquellos productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente devuelva solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Utiliza la función filter() o una lista por comprensión para el filtro, el método .sort() o sorted() con una función lambda para el ordenamiento, y una lista por comprensión para extraer los nombres.

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
    # Filtra stock > 0: Mouse(20), Auriculares(30), Monitor(200). Teclado queda fuera.
    assert procesar_inventario(inventario) == ['Mouse', 'Auriculares', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'Test', 'precio': 10, 'stock': 0}]) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")