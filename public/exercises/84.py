# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos cuyo precio sea superior a 50.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor']
# hint: Utiliza una lista de comprensión para el filtrado inicial, el método .sort() con una función lambda para el ordenamiento, y un último filtro para extraer los nombres finales.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar stock menor a 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio (menor a mayor)
    filtrados.sort(key=lambda x: x['precio'])
    
    # Extraer nombres de productos con precio > 50
    resultado = [p['nombre'] for p in filtrados if p['precio'] > 50]
    
    return resultado

# === TESTS ===
try:
    data = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 60, 'stock': 5},
        {'nombre': 'Cable', 'precio': 10, 'stock': 2}
    ]
    assert procesar_inventario(data) == ['Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")