# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los restantes por precio de forma descendente y busca el nombre del producto más caro.
# difficulty: Intermedio
# expected_output: {'productos_filtrados': [{'nombre': 'Laptop', 'precio': 1200, 'stock': 10}], 'producto_mas_caro': 'Laptop'}
# hint: Usa un filtro (list comprehension o filter), la función sorted con un parámetro key, y para el máximo puedes usar la función max.

# === SOLUTION ===
def gestionar_inventario(productos):
    # Filtrar productos con stock mayor o igual a 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio de forma descendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    
    # Obtener el nombre del producto más caro si la lista no está vacía
    mas_caro = ordenados[0]['nombre'] if ordenados else None
    
    return {
        'productos_filtrados': ordenados,
        'producto_mas_caro': mas_caro
    }

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 8}
    ]
    resultado = gestionar_inventario(inventario)
    assert resultado['producto_mas_caro'] == 'Laptop', "Error: El producto más caro debería ser Laptop."
    assert len(resultado['productos_filtrados']) == 2, "Error: Deberían quedar 2 productos tras filtrar el stock."
    assert resultado['productos_filtrados'][0]['precio'] == 1200, "Error: El orden debería ser descendente por precio."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")