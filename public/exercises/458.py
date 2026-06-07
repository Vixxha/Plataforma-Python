# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (nombre, precio, stock), escribe una función que filtre aquellos productos con stock mayor a cero, los ordene de menor a mayor precio y finalmente retorne únicamente los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Utiliza una lista de comprensión para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y finalmente una comprensión de lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Leche', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Pan', 'precio': 1.0, 'stock': 5},
        {'nombre': 'Huevo', 'precio': 2.0, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 0.5, 'stock': 20}
    ]
    assert procesar_inventario(inventario) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: el caso de stock cero falló."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}, {'nombre': 'A', 'precio': 2, 'stock': 1}]) == ['A', 'B'], "Error: el ordenamiento no es correcto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")