# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, y el parámetro `key` en `sorted()` pasando una tupla para ordenar por múltiples criterios.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    # Filtrar productos por precio mínimo
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    
    # Ordenar primero por precio ascendente, luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados]
    
    return resultado

# === TESTS ===
try:
    inv = [
        {'nombre': 'Zapatos', 'precio': 50},
        {'nombre': 'Gorra', 'precio': 15},
        {'nombre': 'Camisa', 'precio': 25},
        {'nombre': 'Pantalón', 'precio': 25}
    ]
    
    assert procesar_inventario(inv, 25) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 100) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 15) == ['Gorra', 'Camisa', 'Pantalón', 'Zapatos'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")