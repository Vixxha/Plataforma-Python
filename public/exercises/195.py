# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea menor a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (list comprehension o filter), luego el método .sort() o sorted() con una función lambda, y finalmente una extracción de claves.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    disponibles = [p for p in productos if p['stock'] > 0]
    disponibles.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in disponibles if p['precio'] < presupuesto]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 2}
    ]
    assert procesar_inventario(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")