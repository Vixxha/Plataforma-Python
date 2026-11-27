# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, los ordene de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar las funciones filter o listas por comprensión para filtrar, el método sorted con una clave múltiple (tupla) para ordenar, y extraer los nombres al final.

# === SOLUTION ===
def procesar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Zapatos', 'precio': 50},
        {'nombre': 'Gorra', 'precio': 15},
        {'nombre': 'Camisa', 'precio': 30},
        {'nombre': 'Pantalón', 'precio': 30},
        {'nombre': 'Medias', 'precio': 5}
    ]
    
    assert procesar_productos(inventario, 30) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 100) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 0) == ['Medias', 'Gorra', 'Camisa', 'Pantalón', 'Zapatos'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")