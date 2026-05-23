# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los restantes por precio de forma descendente y busca el nombre del producto más caro que cumpla con el stock suficiente.
# difficulty: Intermedio
# expected_output: 'Laptop'
# hint: Usa un filtro (list comprehension o filter) para el stock, el método .sort() con una clave lambda para el ordenamiento y accede al primer elemento tras ordenar.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor o igual a 5
    disponibles = [p for p in productos if p['stock'] >= 5]
    
    if not disponibles:
        return None
    
    # Ordenar descendente por precio
    disponibles.sort(key=lambda x: x['precio'], reverse=True)
    
    # Retornar el nombre del más caro
    return disponibles[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 6}
    ]
    assert procesar_inventario(inventario) == 'Laptop', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 2}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 100, 'stock': 10}, {'nombre': 'C', 'precio': 500, 'stock': 5}]) == 'C', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")