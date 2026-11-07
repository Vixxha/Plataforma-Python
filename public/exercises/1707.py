# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, y la función sorted() con una clave múltiple (lambda) para ordenar.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    # Filtrar productos por precio mínimo
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'USB', 'precio': 15},
        {'nombre': 'Audífonos', 'precio': 45}
    ]
    
    assert procesar_inventario(inventario, 40) == ['USB', 'Audífonos', 'Teclado', 'Monitor'] or procesar_inventario(inventario, 40) == ['Audífonos', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 100) == ['Monitor'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")