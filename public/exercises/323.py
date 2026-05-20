# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos cuyo precio sea superior a 50.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa un ciclo for o list comprehension para filtrar primero, luego aplica el método sort() o la función sorted() con una llave (lambda) para el ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor o igual a 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    # Ordenar por precio de menor a mayor
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Seleccionar solo nombres con precio mayor a 50
    resultado = [p['nombre'] for p in ordenados if p['precio'] > 50]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 60, 'stock': 5},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el caso sin elementos caros falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")