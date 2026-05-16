# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con nombre, precio y stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa un filtro (list comprehension o filter), luego el método .sort() o sorted() con un lambda, y finalmente accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente
    disponibles.sort(key=lambda x: x['precio'])
    
    # Retornar el nombre del más barato si hay existencias, sino None
    return disponibles[0]['nombre'] if disponibles else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")