# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, buscar y devolver el nombre del producto más económico dentro de ese filtro. Si la lista filtrada está vacía, debe retornar una cadena vacía "".
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Puedes usar list comprehensions o filter para el filtro, la función sorted() con una función lambda para ordenar por precio, y acceder al primer elemento del resultado ordenado.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    if not disponibles:
        return ""
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Retornar el nombre del producto más económico
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Mochila", "precio": 45.0, "stock": 0}
    ]
    assert procesar_inventario(inventario_1) == "Lápiz", "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {"nombre": "Laptop", "precio": 800.0, "stock": 0},
        {"nombre": "Mouse", "precio": 25.0, "stock": 2}
    ]
    assert procesar_inventario(inventario_2) == "Mouse", "Error: considera casos límites en tu lógica."
    
    inventario_3 = [
        {"nombre": "Monitor", "precio": 150.0, "stock": 0}
    ]
    assert procesar_inventario(inventario_3) == "", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")