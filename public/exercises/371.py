# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), filtra los productos con precio mayor a 50, ordénalos de menor a mayor precio y devuelve una lista con solo los nombres.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa una lista de comprensión o la función filter() para el filtro, el método .sort() o sorted() con una función lambda para el ordenamiento, y una última comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] > 50]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 80},
        {'nombre': 'Cable', 'precio': 10}
    ]
    assert procesar_inventario(productos_test) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}]) == [], "Error: considera casos donde no hay elementos que cumplan el filtro."
    assert procesar_inventario([{'nombre': 'B', 'precio': 60}, {'nombre': 'A', 'precio': 55}]) == ['A', 'B'], "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")