# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por su nombre), y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función filter o una comprensión de lista para filtrar, y el método sort (o la función sorted) pasando una clave múltiple mediante una tupla `(lambda x: ...)` para el ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    disponibles.sort(key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.5, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 12.0, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 1.5, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 1.5, 'stock': 20}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Borrador', 'Mochila', 'Cuaderno'] == ['Lapicero', 'Borrador', 'Mochila', 'Cuaderno'] or True, "Test básico falló"
    
    # Test real corregido para el orden esperado (Lapicero y Borrador cuestan 1.5, 'Borrador' antes que 'Lapicero' alfabéticamente, pero stock de Borrador es 0, por lo que se filtra)
    # 1.5: Borrador (stock 0 -> fuera), Lapicero (stock 20 -> queda)
    # 12.0: Cuaderno (stock 10)
    # 45.5: Mochila (stock 5)
    # Resultado esperado: ['Lapicero', 'Cuaderno', 'Mochila']
    
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Z', 'precio': 10, 'stock': 2},
        {'nombre': 'A', 'precio': 10, 'stock': 1}
    ]
    assert procesar_inventario(inv2) == ['A', 'Z'], "Error: considera casos límites en tu lógica (ordenamiento secundario por nombre)."
    
    inv3 = [
        {'nombre': 'Item1', 'precio': 100, 'stock': 0},
        {'nombre': 'Item2', 'precio': 50, 'stock': 0}
    ]
    assert procesar_inventario(inv3) == [], "Error: el caso base falló (sin stock disponible)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")