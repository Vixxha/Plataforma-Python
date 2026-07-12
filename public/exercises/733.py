# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con nombre, precio y stock), filtra aquellos con stock mayor a cero, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea menor a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (o list comprehension), el método sort o la función sorted con una clave lambda, y finalmente una búsqueda o filtrado adicional.

# === SOLUTION ===
def filtrar_y_ordenar_productos(inventario, presupuesto):
    disponibles = [p for p in inventario if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    resultado = [p['nombre'] for p in ordenados if p['precio'] < presupuesto]
    return resultado

# === TESTS ===
try:
    inventario_test = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Impresora', 'precio': 150, 'stock': 0}
    ]
    assert filtrar_y_ordenar_productos(inventario_test, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario_test, 10) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos([], 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")