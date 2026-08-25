# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos cuyo stock sea mayor a 0, ordenarlos de menor a mayor precio (y alfabéticamente por nombre en caso de empate), y finalmente buscar y devolver una lista únicamente con los nombres de los primeros `n` productos resultantes.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la función `filter` o una comprensión de lista para el filtrado, la función `sorted` con una clave múltiple (tupla) para el ordenamiento, y luego extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, n):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio (ascendente) y luego por nombre (alfabéticamente)
    ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer los nombres de los primeros n productos
    resultado = [p['nombre'] for p in ordenados[:n]]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 2}
    ]
    
    assert procesar_inventario(inv1, 2) == ['Teclado', 'Webcam'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 3) == ['Teclado', 'Webcam', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")