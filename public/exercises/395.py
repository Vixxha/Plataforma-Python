# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre' y 'precio'), implementa una función que filtre los productos con un precio superior a un valor dado, los ordene de menor a mayor precio y finalmente devuelva solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Usa una lista de comprensión o filter() para el filtrado, el método sort() o la función sorted() con una lambda para ordenar, y una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_productos(inventario, precio_minimo):
    productos_filtrados = [p for p in inventario if p['precio'] > precio_minimo]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Teclado', 'precio': 20},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Monitor', 'precio': 150}
    ]
    assert filtrar_y_ordenar_productos(inventario_ejemplo, 100) == ['Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario_ejemplo, 1000) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario_ejemplo, 0) == ['Mouse', 'Teclado', 'Monitor', 'Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")