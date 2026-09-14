# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente buscar y devolver una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una clave múltiple (tupla) para ordenar, y finalmente extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_max):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inventario_test = [
        {'nombre': 'Arroz', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Leche', 'precio': 15.5, 'stock': 5},
        {'nombre': 'Pan', 'precio': 5.0, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 5.0, 'stock': 20},
        {'nombre': 'Carne', 'precio': 50.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_test, 20.0) == ['Manzana', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_test, 5.0) == ['Manzana'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_test, 100.0) == ['Manzana', 'Leche', 'Arroz', 'Carne'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")