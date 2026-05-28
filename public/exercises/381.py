# === METADATA ===
# title: Gestión de Inventario Tech
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos de menor a mayor precio y finalmente busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: 'Mouse'
# hint: Usa un filtro (o comprensión de listas), el método sorted() con una llave lambda y, tras ordenar, accede al primer elemento.

# === SOLUTION ===
def procesar_inventario(productos):
    # 1. Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # 2. Ordenar por precio (ascendente)
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # 3. Retornar el nombre del primero (el más barato) o None si está vacío
    return ordenados[0]['nombre'] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == 'Mouse', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 100, 'stock': 0}]) == None, "Error: considera casos donde no hay stock."
    assert procesar_inventario([{'nombre': 'B', 'precio': 10, 'stock': 1}, {'nombre': 'A', 'precio': 5, 'stock': 1}]) == 'A', "Error: el ordenamiento no es correcto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")