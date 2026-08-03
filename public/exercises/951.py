# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista únicamente con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar list comprehensions o filter para el filtrado, el método sorted() con una clave múltiple (lambda x: (x['precio'], x['nombre'])) para ordenar, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    productos_filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Zapatos', 'precio': 50},
        {'nombre': 'Gorra', 'precio': 15},
        {'nombre': 'Camisa', 'precio': 30},
        {'nombre': 'Pantalón', 'precio': 30}
    ]
    assert procesar_inventario(inv1, 30) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 100) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv1, 10) == ['Gorra', 'Camisa', 'Pantalón', 'Zapatos'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")