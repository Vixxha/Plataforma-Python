# === METADATA ===
# title: Gestión y Filtrado de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a 5, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes. Si dos productos tienen el mismo precio, mantén el orden relativo original o el que determine Python.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado', 'Mouse']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento por precio descendente, y otra compresión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p.get('stock', 0) > 5]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 3},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 8},
        {'nombre': 'Monitor', 'precio': 250.0, 'stock': 2}
    ]
    assert procesar_inventario(inventario_1) == ['Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'A', 'precio': 10, 'stock': 6},
        {'nombre': 'B', 'precio': 30, 'stock': 6},
        {'nombre': 'C', 'precio': 20, 'stock': 6}
    ]
    assert procesar_inventario(inventario_2) == ['B', 'C', 'A'], "Error: considera casos límites en tu lógica."
    
    assert procesar_inventario([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")