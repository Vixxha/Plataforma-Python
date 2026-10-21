# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 40, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Auriculares', 'Mouse', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 0},
        {'nombre': 'USB', 'precio': 10, 'stock': 15}
    ]
    assert procesar_inventario(inv2) == ['USB'], "Error: considera casos límites en tu lógica."
    
    assert procesar_inventario([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")