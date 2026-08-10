# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor al mínimo requerido, ordenarlos de forma descendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Teclado', 'Mouse']
# hint: Puedes usar la función `filter` o listas por comprensión para filtrar, el método `.sort()` o la función `sorted()` con una tupla en el parámetro `key` para ordenar con múltiples criterios, y otra lista por comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    # Filtrar productos con stock mayor al mínimo
    filtrados = [p for p in productos if p['stock'] > stock_minimo]
    
    # Ordenar por precio descendente (-p['precio']) y por nombre ascendente (p['nombre'])
    ordenados = sorted(filtrados, key=lambda x: (-x['precio'], x['nombre']))
    
    # Extraer únicamente los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 8},
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inv, 4) == ['Laptop', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 15) == [], "Error: considera casos límites en tu lógica."
    
    inv_empate = [
        {'nombre': 'Zeta', 'precio': 50.0, 'stock': 10},
        {'nombre': 'Alfa', 'precio': 50.0, 'stock': 12}
    ]
    assert procesar_inventario(inv_empate, 5) == ['Alfa', 'Zeta'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")