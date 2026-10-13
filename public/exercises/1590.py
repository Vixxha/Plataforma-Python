# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de menor a mayor precio (y en caso de empate, alfabéticamente por nombre) y retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno']
# hint: Puedes usar 'filter' o list comprehensions para la condición de stock y presupuesto, y la función 'sorted' con una clave múltiple (tupla) para el ordenamiento.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto_max):
    # Filtrar productos con stock > 0 y precio <= presupuesto_max
    filtrados = [
        p for p in productos 
        if p.get('stock', 0) > 0 and p.get('precio', 0) <= presupuesto_max
    ]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 12.5, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 2.0, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.0, 'stock': 15},
        {'nombre': 'Calculadora', 'precio': 25.0, 'stock': 2}
    ]
    
    assert filtrar_y_ordenar_productos(inventario, 15.0) == ['Lapicero', 'Cuaderno'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 2.0) == ['Lapicero'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 1.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")