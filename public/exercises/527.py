# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con nombre, precio y stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve solo los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Usa una lista de comprensión o filter() para la primera condición, sorted() con una lambda para ordenar, y una segunda lista de comprensión para extraer los nombres finales.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # 1. Filtrar stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # 2. Ordenar por precio
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # 3. Filtrar por límite de precio y extraer nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] < limite_precio]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Auriculares', 'precio': 30, 'stock': 2}
    ]
    assert procesar_inventario(inventario, 100) == ['Mouse', 'Auriculares'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")