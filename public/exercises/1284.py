# === METADATA ===
# title: Gestión y Búsqueda de Productos en el Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento por 'precio', y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 15.0, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 45.0, 'stock': 2}
    ]
    assert procesar_inventario(inventario_1) == ['Audífonos', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'Laptop', 'precio': 1000.0, 'stock': 0},
        {'nombre': 'Cable HDMI', 'precio': 10.0, 'stock': 15}
    ]
    assert procesar_inventario(inventario_2) == ['Cable HDMI'], "Error: considera casos límites en tu lógica."
    
    inventario_3 = []
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")