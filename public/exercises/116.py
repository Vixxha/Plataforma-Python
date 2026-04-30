# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos productos cuyo precio sea superior a 100.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Usa una lista de comprensión para filtrar el stock, luego emplea el método .sort() o la función sorted() con una expresión lambda para ordenar por precio.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock >= 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio (menor a mayor)
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Extraer nombres de productos con precio > 100
    resultado = [p['nombre'] for p in ordenados if p['precio'] > 100]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 8},
        {'nombre': 'Mouse', 'precio': 30, 'stock': 2},
        {'nombre': 'Laptop', 'precio': 800, 'stock': 5}
    ]
    assert procesar_inventario(inventario) == ['Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 150, 'stock': 1}]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 200, 'stock': 10}]) == ['B'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")