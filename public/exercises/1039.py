# === METADATA ===
# title: Gestión y Filtrado de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a 0, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por el nombre) y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función filter() o listas de comprensión, el método sorted() con una clave múltiple (tupla) y extraer los nombres mediante una comprensión de listas.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 15.00, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 2.00, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.00, 'stock': 25}
    ]
    assert procesar_inventario(inventario_1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inventario_2 = [
        {'nombre': 'Tablet', 'precio': 300.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 2}
    ]
    assert procesar_inventario(inventario_2) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    inventario_3 = []
    assert procesar_inventario(inventario_3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")