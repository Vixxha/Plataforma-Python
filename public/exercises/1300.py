# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por el nombre) y finalmente retornar una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar la función `filter()` o una comprensión de listas para filtrar, y la función `sorted()` con una función `lambda` o una tupla de ordenamiento para ordenar por múltiples criterios.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    productos_ordenados = sorted(productos_filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Leche', 'precio': 1.2, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 0.8, 'stock': 0},
        {'nombre': 'Carne', 'precio': 5.0, 'stock': 2}
    ]
    assert procesar_inventario(inventario_1) == ['Leche', 'Pan', 'Carne'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'Zapatos', 'precio': 50.0, 'stock': 4},
        {'nombre': 'Camisa', 'precio': 20.0, 'stock': 0},
        {'nombre': 'Gorra', 'precio': 20.0, 'stock': 10}
    ]
    assert procesar_inventario(inventario_2) == ['Gorra', 'Zapatos'], "Error: considera casos límites en tu lógica (empates de precio)."
    
    inventario_3 = [
        {'nombre': 'Tablet', 'precio': 300.0, 'stock': 0},
        {'nombre': 'Cable', 'precio': 5.0, 'stock': 0}
    ]
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló cuando no hay stock disponible."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")