# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: {'producto_mas_barato': 'Mouse', 'lista_filtrada_y_ordenada': [{'nombre': 'Mouse', 'precio': 15, 'stock': 10}, {'nombre': 'Teclado', 'precio': 45, 'stock': 5}]}
# hint: Usa un list comprehension para filtrar, la función sorted() con un parámetro 'key' para ordenar, y accede al primer elemento de la lista resultante para el más barato.

# === SOLUTION ===
def gestionar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio (ascendente)
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Buscar el más barato
    mas_barato = ordenados[0]['nombre'] if ordenados else None
    
    return {
        'producto_mas_barato': mas_barato,
        'lista_filtrada_y_ordenada': ordenados
    }

# === TESTS ===
try:
    data = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 15, 'stock': 10}
    ]
    resultado = gestionar_inventario(data)
    assert resultado['producto_mas_barato'] == 'Mouse', "Error: El nombre del producto más barato es incorrecto."
    assert len(resultado['lista_filtrada_y_ordenada']) == 2, "Error: El filtro de stock falló."
    assert resultado['lista_filtrada_y_ordenada'][0]['precio'] == 15, "Error: El ordenamiento por precio es incorrecto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")