# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con nombre, precio y cantidad), implementa una función que filtre los productos con un precio menor a 50, los ordene de forma descendente según su cantidad y devuelva solo los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Primero usa una lista por comprensión para filtrar, luego el método .sort() o la función sorted() con una llave lambda para ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p['precio'] < 50]
    filtrados.sort(key=lambda x: x['cantidad'], reverse=True)
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 800, 'cantidad': 5},
        {'nombre': 'Mouse', 'precio': 20, 'cantidad': 10},
        {'nombre': 'Teclado', 'precio': 30, 'cantidad': 15},
        {'nombre': 'Monitor', 'precio': 150, 'cantidad': 2}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'Cable', 'precio': 10, 'cantidad': 1}]) == ['Cable'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")