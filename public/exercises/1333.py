# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista solo con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una clave múltiple (tupla) para el ordenamiento, y otra comprensión de lista para extraer solo los nombres.

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
        {'nombre': 'Camisa', 'precio': 25},
        {'nombre': 'Pantalón', 'precio': 40},
        {'nombre': 'Cinturón', 'precio': 15}
    ]
    
    assert procesar_productos(inventario, 20) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 50) == ['Zapatos'], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")