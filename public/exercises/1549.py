# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a 0, ordenarlos de forma ascendente según su 'precio', y finalmente buscar y devolver una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno']
# hint: Primero filtra la lista usando una comprensión de lista o filter, luego ordena la lista filtrada usando sorted con una función lambda, y finalmente extrae los nombres de los elementos que cumplan con el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    resultado = [p['nombre'] for p in productos_ordenados if p['precio'] <= presupuesto_maximo]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mochila', 'precio': 45.0, 'stock': 5},
        {'nombre': 'Lapicero', 'precio': 1.5, 'stock': 100},
        {'nombre': 'Cuaderno', 'precio': 3.0, 'stock': 0},
        {'nombre': 'Borrador', 'precio': 0.8, 'stock': 50}
    ]
    
    assert procesar_inventario(inventario, 5.0) == ['Borrador', 'Lapicero'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 1.0) == ['Borrador'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 0.5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")