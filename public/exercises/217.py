# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: {'producto_mas_barato': 'Teclado', 'lista_ordenada': [{'nombre': 'Teclado', 'precio': 20}, {'nombre': 'Monitor', 'precio': 150}]}
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y accede al primer índice para encontrar el mínimo.

# === SOLUTION ===
def gestionar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    resultado = {
        'producto_mas_barato': ordenados[0]['nombre'] if ordenados else None,
        'lista_ordenada': [{'nombre': p['nombre'], 'precio': p['precio']} for p in ordenados]
    }
    return resultado

# === TESTS ===
try:
    data = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 20, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 5}
    ]
    resultado_esperado = {
        'producto_mas_barato': 'Teclado', 
        'lista_ordenada': [{'nombre': 'Teclado', 'precio': 20}, {'nombre': 'Monitor', 'precio': 150}]
    }
    assert gestionar_inventario(data) == resultado_esperado, "Error: la lógica de filtrado u ordenamiento es incorrecta."
    assert gestionar_inventario([])['producto_mas_barato'] == None, "Error: debe manejar listas vacías."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")