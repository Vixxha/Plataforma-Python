# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (nombre y precio), escribe una función que filtre aquellos productos con un precio mayor o igual a un umbral, los ordene de menor a mayor por precio y retorne únicamente los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Utiliza una lista de comprensión (list comprehension) para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y finalmente recorre la lista para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, umbral):
    filtrados = [p for p in productos if p['precio'] >= umbral]
    filtrados.sort(key=lambda x: x['precio'])
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Cable', 'precio': 5}
    ]
    assert procesar_inventario(inventario, 40) == ['Teclado', 'Monitor'], "Error: el filtro o el ordenamiento es incorrecto."
    assert procesar_inventario(inventario, 200) == [], "Error: debería retornar una lista vacía si no hay coincidencias."
    assert procesar_inventario(inventario, 0) == ['Cable', 'Mouse', 'Teclado', 'Monitor'], "Error: el caso base con umbral 0 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")