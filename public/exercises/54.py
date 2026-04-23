# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dada una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y busca el nombre del producto más barato dentro de ese subconjunto filtrado.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa una lista de comprensión para el filtro, la función sorted() con una lambda para el ordenamiento y accede al primer elemento de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock menor a 5
    bajo_stock = [p for p in productos if p['stock'] < 5]
    
    if not bajo_stock:
        return None
    
    # Ordenar por precio ascendente
    ordenados = sorted(bajo_stock, key=lambda x: x['precio'])
    
    # Retornar el nombre del más barato
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 15, 'stock': 3},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 1}
    ]
    assert procesar_inventario(inventario) == "Teclado", "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'USB', 'precio': 10, 'stock': 10}]) == None, "Error: debe retornar None si no hay stock bajo."
    assert procesar_inventario([{'nombre': 'A', 'precio': 100, 'stock': 0}, {'nombre': 'B', 'precio': 50, 'stock': 0}]) == "B", "Error: el ordenamiento falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")