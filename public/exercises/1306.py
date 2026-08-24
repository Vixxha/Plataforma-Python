# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan stock mayor a cero, ordenarlos por precio de menor a mayor (y en caso de empate, alfabéticamente por nombre) y finalmente buscar y retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno']
# hint: Puedes usar las funciones integradas filter() o listas por comprensión para filtrar, sorted() con una clave múltiple (tupla) para ordenar, y luego extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar aquellos cuyo precio sea menor o igual al presupuesto y extraer sus nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 12.5, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 2.0, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 2.0, 'stock': 15}
    ]
    assert procesar_inventario(inv1, 15.0) == ['Borrador', 'Lapicero', 'Cuaderno'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 5.0) == ['Borrador', 'Lapicero'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv1, 1.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")