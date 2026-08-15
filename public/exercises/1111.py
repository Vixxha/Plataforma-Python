# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente, y finalmente devolver una lista con los nombres de los primeros N productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar list comprehensions o filter para la condición, la función sorted con una función lambda para ordenar, y realizar una búsqueda por corte (slicing) para limitar la cantidad de elementos devueltos.

# === SOLUTION ===
def procesar_inventario(productos, n):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Extraer los nombres de los primeros n productos
    resultado = [p['nombre'] for p in ordenados[:n]]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Monitor', 'precio': 200.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Laptop', 'precio': 850.0, 'stock': 2},
        {'nombre': 'Cable HDMI', 'precio': 10.0, 'stock': 15}
    ]
    
    assert procesar_inventario(inventario_prueba, 3) == ['Cable HDMI', 'Mouse', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 1) == ['Cable HDMI'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 2) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")