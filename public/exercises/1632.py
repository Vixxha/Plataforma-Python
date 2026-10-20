# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a un valor mínimo dado, ordenarlos de forma ascendente según su precio (y en caso de empate, alfabéticamente por su nombre) y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor', 'Teclado']
# hint: Puedes usar la función filter() o una list comprehension para filtrar, y el parámetro key de sorted() con una tupla para ordenar por múltiples criterios.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p['stock'] > stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 5},
        {"nombre": "Laptop", "precio": 800.0, "stock": 10},
        {"nombre": "Teclado", "precio": 45.0, "stock": 15},
        {"nombre": "Monitor", "precio": 150.0, "stock": 8}
    ]
    
    assert procesar_inventario(inv, 6) == ['Teclado', 'Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 20) == [], "Error: considera casos límites en tu lógica."
    
    inv_empate = [
        {"nombre": "Zeta", "precio": 50.0, "stock": 10},
        {"nombre": "Alfa", "precio": 50.0, "stock": 10}
    ]
    assert procesar_inventario(inv_empate, 5) == ['Alfa', 'Zeta'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")