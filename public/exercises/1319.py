# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo, ordene los resultados resultantes de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista únicamente con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Café', 'Te', 'Azúcar']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una tupla en el parámetro `key` para ordenar por múltiples criterios, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Azúcar', 'precio': 15},
        {'nombre': 'Café', 'precio': 10},
        {'nombre': 'Leche', 'precio': 20},
        {'nombre': 'Te', 'precio': 10}
    ]
    
    assert procesar_productos(inventario, 10) == ['Café', 'Te', 'Azúcar', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 18) == ['Leche'], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 30) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")