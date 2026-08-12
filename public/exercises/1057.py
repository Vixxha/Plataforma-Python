# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos ordenados que cumplan con la condición.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la comprensión de listas o la función filter() para la condición, el método sorted() con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Monitor', 'precio': 200.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50.0, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 45.0, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Audífonos', 'Mouse', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 0},
        {'nombre': 'Cable HDMI', 'precio': 15.0, 'stock': 20}
    ]
    assert procesar_inventario(inv2) == ['Cable HDMI'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")