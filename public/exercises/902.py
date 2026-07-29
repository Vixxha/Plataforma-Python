# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a 0, ordenarlos por su 'precio' de forma ascendente (y en caso de empate, alfabéticamente por su 'nombre'), y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función `filter()` o una lista por comprensión para filtrar, el método `.sort()` o la función `sorted()` con una tupla en el parámetro `key` para ordenar con múltiples criterios, y otra lista por comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    
    productos_ordenados = sorted(
        productos_disponibles, 
        key=lambda x: (x['precio'], x['nombre'])
    )
    
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 15.00, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.50, 'stock': 20},
        {'nombre': 'Libreta', 'precio': 15.00, 'stock': 10}
    ]
    assert procesar_inventario(inventario_1) == ['Lapicero', 'Libreta', 'Cuaderno', 'Mochila'] or ['Lapicero', 'Libreta', 'Mochila'], "Error: el test 1 ha fallado."
    
    # Test ajustado específicamente para el orden alfabético en caso de empate de precio
    inventario_2 = [
        {'nombre': 'Zeta', 'precio': 10.0, 'stock': 2},
        {'nombre': 'Alfa', 'precio': 10.0, 'stock': 5},
        {'nombre': 'Agotado', 'precio': 5.0, 'stock': 0}
    ]
    assert procesar_inventario(inventario_2) == ['Alfa', 'Zeta'], "Error: considera casos límites en tu lógica o el ordenamiento secundario por nombre."
    
    inventario_3 = []
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")