# === METADATA ===
# title: Gestión de Inventario Inteligente
# description: Dado una lista de diccionarios (productos con nombre, precio y cantidad), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos que cuestan menos de un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan']
# hint: Usa un bucle o list comprehension para filtrar por stock, el método .sort() o sorted() con una función lambda para el precio, y otro filtro para el presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_inventario(productos, presupuesto):
    # Filtrar por stock > 0
    disponibles = [p for p in productos if p['cantidad'] > 0]
    # Ordenar por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    # Filtrar por presupuesto y extraer solo nombres
    resultado = [p['nombre'] for p in disponibles if p['precio'] < presupuesto]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Leche', 'precio': 15, 'cantidad': 0},
        {'nombre': 'Pan', 'precio': 5, 'cantidad': 10},
        {'nombre': 'Manzana', 'precio': 2, 'cantidad': 5},
        {'nombre': 'Carne', 'precio': 20, 'cantidad': 2}
    ]
    assert filtrar_y_ordenar_inventario(inventario, 10) == ['Manzana', 'Pan'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_inventario(inventario, 1) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")