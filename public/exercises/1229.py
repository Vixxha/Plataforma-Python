# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted con una función lambda para ordenar, y otra pasada para extraer los nombres según el límite de precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por el límite de precio y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= limite_precio]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 30, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_prueba, 50) == ['Mouse', 'Audífonos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 20) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")