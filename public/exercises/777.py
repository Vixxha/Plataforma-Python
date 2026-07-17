# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (nombre y precio), escribe una función que filtre los productos con un precio mayor a un valor dado, los ordene alfabéticamente por nombre y devuelva una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse']
# hint: Puedes usar la función filter() o una comprensión de listas, seguido del método .sort() o la función sorted() con una clave personalizada.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    # Filtrar productos cuyo precio sea mayor al mínimo
    filtrados = [p for p in productos if p['precio'] > precio_minimo]
    # Ordenar por nombre
    filtrados.sort(key=lambda x: x['nombre'])
    # Retornar solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 15},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Monitor', 'precio': 150}
    ]
    assert procesar_inventario(inventario, 20) == ['Laptop', 'Monitor', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 500) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 1000) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")