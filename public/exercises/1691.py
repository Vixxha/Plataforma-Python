# === METADATA ===
# title: Gestión de Inventario: Filtrado, Ordenamiento y Búsqueda
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'). La función debe filtrar los productos cuyo stock sea mayor al valor mínimo dado, ordenarlos de forma descendente según su precio (y en caso de empate, alfabéticamente por su nombre) y finalmente retornar únicamente una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado', 'Mouse']
# hint: Puedes usar la función `filter` o listas por comprensión para el filtrado, y el método `sorted` con una tupla en el parámetro `key` para manejar múltiples criterios de ordenamiento.

# === SOLUTION ===
def gestionar_inventario(productos, stock_minimo):
    # Filtrar productos con stock mayor al mínimo
    filtrados = [p for p in productos if p['stock'] > stock_minimo]
    
    # Ordenar: primero por precio descendente (-x['precio']), luego por nombre ascendente (x['nombre'])
    ordenados = sorted(filtrados, key=lambda x: (-x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Teclado", "precio": 45.0, "stock": 5},
        {"nombre": "Monitor", "precio": 150.0, "stock": 2},
        {"nombre": "Laptop", "precio": 800.0, "stock": 8},
        {"nombre": "USB", "precio": 25.5, "stock": 15}
    ]
    
    assert gestionar_inventario(inv, 4) == ['Laptop', 'Teclado', 'USB', 'Mouse'], "Error: el test 1 ha fallado."
    assert gestionar_inventario(inv, 12) == ['USB'], "Error: considera casos límites en tu lógica."
    assert gestionar_inventario(inv, 50) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")