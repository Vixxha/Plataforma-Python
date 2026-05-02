# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los restantes por precio de menor a mayor, y realiza una búsqueda para retornar el nombre del producto más caro que tenga al menos 10 unidades.
# difficulty: Intermedio
# expected_output: {'filtrados': [{'nombre': 'Teclado', 'precio': 20, 'stock': 20}], 'mas_caro': 'Teclado'}
# hint: Usa un filtro (comprensión de listas) para el stock, el método sort() o sorted() para ordenar, y max() con un key para la búsqueda.

# === SOLUTION ===
def gestionar_inventario(productos):
    # Filtrar productos con stock >= 5
    disponibles = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio de menor a mayor
    disponibles_ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Buscar el más caro con stock >= 10
    con_stock_alto = [p for p in disponibles if p['stock'] >= 10]
    mas_caro = max(con_stock_alto, key=lambda x: x['precio']) if con_stock_alto else None
    
    return {
        'filtrados': disponibles_ordenados,
        'mas_caro': mas_caro['nombre'] if mas_caro else None
    }

# === TESTS ===
try:
    datos = [
        {'nombre': 'Mouse', 'precio': 50, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 20, 'stock': 20},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 15}
    ]
    resultado = gestionar_inventario(datos)
    assert resultado['filtrados'][0]['nombre'] == 'Teclado', "Error: el ordenamiento por precio es incorrecto."
    assert resultado['mas_caro'] == 'Monitor', "Error: el cálculo del producto más caro falló."
    assert len(resultado['filtrados']) == 2, "Error: el filtrado de stock menor a 5 falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")