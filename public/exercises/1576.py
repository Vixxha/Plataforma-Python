# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos cuyo stock sea mayor a 0, ordenarlos por precio de forma ascendente (y en caso de empate en precio, alfabéticamente por nombre), y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar la función `filter` o una comprensión de lista para el filtrado, y la función `sorted` con una tupla en el parámetro `key` para manejar múltiples criterios de ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Leche', 'precio': 1.2, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 1.2, 'stock': 20},
        {'nombre': 'Carne', 'precio': 5.0, 'stock': 0}
    ]
    assert procesar_inventario(inv1) == ['Leche', 'Manzana', 'Pan'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Zapatos', 'precio': 50.0, 'stock': 2},
        {'nombre': 'Camisa', 'precio': 20.0, 'stock': 0}
    ]
    assert procesar_inventario(inv2) == ['Zapatos'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")