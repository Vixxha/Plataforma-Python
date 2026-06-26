# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos cuyo precio sea superior a 50.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Usa una lista de comprensión o filter() para la condición inicial, el método .sort() o sorted() con una función lambda para el ordenamiento, y finalmente una comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock >= 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Extraer nombres de productos con precio > 50
    resultado = [p['nombre'] for p in ordenados if p['precio'] > 50]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 80, 'stock': 6},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == [], "Error: el caso de stock insuficiente falló."
    assert procesar_inventario([{'nombre': 'B', 'precio': 100, 'stock': 10}]) == ['B'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")