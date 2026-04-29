# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y finalmente implementa una búsqueda por nombre que devuelva el precio del producto si existe, o None si no se encuentra.
# difficulty: Intermedio
# expected_output: {'productos_ordenados': [{'nombre': 'mouse', 'precio': 20, 'stock': 10}, {'nombre': 'teclado', 'precio': 45, 'stock': 5}], 'precio_buscado': 45}
# hint: Usa 'filter' o una lista de comprensión para el stock, el método '.sort()' o 'sorted()' para el ordenamiento y una iteración simple o comprensión para la búsqueda.

# === SOLUTION ===
def procesar_inventario(inventario, nombre_busqueda):
    disponibles = [p for p in inventario if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    precio_encontrado = None
    for p in ordenados:
        if p['nombre'] == nombre_busqueda:
            precio_encontrado = p['precio']
            break
            
    return {"productos_ordenados": ordenados, "precio_buscado": precio_encontrado}

# === TESTS ===
try:
    data = [
        {'nombre': 'monitor', 'precio': 200, 'stock': 0},
        {'nombre': 'teclado', 'precio': 45, 'stock': 5},
        {'nombre': 'mouse', 'precio': 20, 'stock': 10}
    ]
    resultado = procesar_inventario(data, 'teclado')
    assert len(resultado['productos_ordenados']) == 2, "Error: El filtrado de stock falló."
    assert resultado['productos_ordenados'][0]['nombre'] == 'mouse', "Error: El ordenamiento por precio falló."
    assert resultado['precio_buscado'] == 45, "Error: La búsqueda por nombre falló."
    assert procesar_inventario(data, 'cámara')['precio_buscado'] is None, "Error: La búsqueda de un inexistente debería retornar None."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")