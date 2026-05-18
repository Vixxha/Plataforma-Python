# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos que cuesten más de 50, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y finalmente recorre la lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] > 50]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    assert procesar_inventario([{'nombre': 'Mouse', 'precio': 60}, {'nombre': 'Cable', 'precio': 10}, {'nombre': 'Monitor', 'precio': 200}, {'nombre': 'Teclado', 'precio': 80}]) == ['Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10}, {'nombre': 'B', 'precio': 20}]) == [], "Error: debe devolver lista vacía si nada cumple la condición."
    assert procesar_inventario([{'nombre': 'Pro', 'precio': 500}, {'nombre': 'Mini', 'precio': 100}]) == ['Mini', 'Pro'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")