# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (nombre y precio), crea una función que filtre los productos con un precio mayor o igual a un valor mínimo dado y devuelva la lista ordenada alfabéticamente por nombre.
# difficulty: Intermedio
# expected_output: [{'nombre': 'Laptop', 'precio': 1200}, {'nombre': 'Monitor', 'precio': 300}]
# hint: Puedes usar la función filter() o una comprensión de listas para el filtrado, y el método sort() o la función sorted() con una llave lambda para el ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    return sorted(filtrados, key=lambda x: x['nombre'])

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Teclado', 'precio': 20},
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Monitor', 'precio': 300}
    ]
    assert procesar_inventario(inventario, 100) == [{'nombre': 'Laptop', 'precio': 1200}, {'nombre': 'Monitor', 'precio': 300}], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 500) == [{'nombre': 'Laptop', 'precio': 1200}], "Error: considera casos con un solo elemento."
    assert procesar_inventario(inventario, 2000) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función procesar_inventario no está definida. Verifica el nombre.")