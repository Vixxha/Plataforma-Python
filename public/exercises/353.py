# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del primer producto que sea más barato de 50 unidades monetarias. Si no existe ninguno, retorna None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa un filtro (list comprehension o filter), luego el método .sort() o la función sorted() con una lambda, y finalmente realiza una búsqueda simple.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    for p in ordenados:
        if p['precio'] < 50:
            return p['nombre']
    return None

# === TESTS ===
try:
    productos_test = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 10},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(productos_test) == 'Cable', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'GPU', 'precio': 800, 'stock': 1}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([]) == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")