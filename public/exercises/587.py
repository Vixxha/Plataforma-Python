# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos encontrados que cuesten menos de un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Usa un bucle o list comprehension para filtrar por stock, el método .sort() o sorted() con una función lambda para el ordenamiento, y un último filtro para el presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_productos(inventario, presupuesto):
    productos_disponibles = [p for p in inventario if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados if p['precio'] < presupuesto]

# === TESTS ===
try:
    inventario_test = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 40, 'stock': 2}
    ]
    assert filtrar_y_ordenar_productos(inventario_test, 100) == ['Mouse', 'Auriculares'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario_test, 10) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos([], 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")