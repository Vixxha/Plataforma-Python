# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, buscar y retornar el nombre del producto más económico dentro de ese subconjunto filtrado. Si la lista filtrada está vacía, debe retornar una cadena indicando "Inventario vacío".
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Puedes usar list comprehensions o filter para descartar los productos sin stock, la función sorted() con una función lambda para ordenar por precio, y acceder al primer elemento si existe.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not disponibles:
        return "Inventario vacío"
    
    # Ordenar por precio de forma ascendente
    disponibles_ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Retornar el nombre del producto más económico
    return disponibles_ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Mochila", "precio": 45.0, "stock": 0}
    ]
    inventario_2 = [
        {"nombre": "Borrador", "precio": 1.5, "stock": 0},
        {"nombre": "Regla", "precio": 3.0, "stock": 0}
    ]
    inventario_3 = [
        {"nombre": "Goma", "precio": 1.0, "stock": 2},
        {"nombre": "Bolígrafo", "precio": 1.5, "stock": 25}
    ]
    
    assert procesar_inventario(inventario_1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_2) == "Inventario vacío", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_3) == "Goma", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")