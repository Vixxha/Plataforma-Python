# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente buscar y devolver una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar la función `filter` o una comprensión de listas para filtrar, la función `sorted` con una clave múltiple (tupla) para ordenar, y otra pasada para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos con stock mayor a 0
    con_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(con_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Arroz', 'precio': 15.0, 'stock': 10},
        {'nombre': 'Leche', 'precio': 5.0, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 2.0, 'stock': 20},
        {'nombre': 'Pan', 'precio': 3.5, 'stock': 0},
        {'nombre': 'Carne', 'precio': 15.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_prueba, 10.0) == ['Manzana', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 20.0) == ['Manzana', 'Leche', 'Arroz', 'Carne'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_prueba, 1.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")