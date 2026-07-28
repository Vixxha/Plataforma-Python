# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente retornar una lista únicamente con los nombres de los productos que cumplan con la condición y cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar la función `filter` o listas por comprensión para filtrar, el método `sorted` con una clave múltiple (tupla) para ordenar, y asegurar que buscas según el límite de precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar productos con stock > 0 y precio <= limite_precio
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= limite_precio]
    
    # Ordenar primero por precio (ascendente) y luego por nombre (alfabéticamente)
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2},
        {'nombre': 'Audífonos', 'precio': 25, 'stock': 8}
    ]
    
    assert procesar_inventario(inv, 50) == ['Audífonos', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 200) == ['Audífonos', 'Mouse', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")