# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (nombre y precio), crea una función que filtre aquellos productos con un precio mayor o igual a un umbral, los ordene de menor a mayor precio y finalmente devuelva solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Utiliza una lista de comprensión o filter() para filtrar, el método sorted() o .sort() con un parámetro 'key' para ordenar por precio, y finalmente una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, umbral):
    filtrados = [p for p in productos if p['precio'] >= umbral]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Teclado', 'precio': 20},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Monitor', 'precio': 150}
    ]
    assert procesar_inventario(inventario, 100) == ['Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 500) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 1000) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")