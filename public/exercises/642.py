# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del producto más barato.
# difficulty: Intermedio
# expected_output: {'producto_mas_barato': 'Mouse', 'inventario_filtrado': [{'nombre': 'Mouse', 'precio': 15}, {'nombre': 'Teclado', 'precio': 30}]}
# hint: Usa un filtro de lista o la función filter(), luego aplica el método sort() o la función sorted() con una llave lambda, y finalmente accede al primer índice de la lista resultante.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    resultado = {
        'producto_mas_barato': ordenados[0]['nombre'] if ordenados else None,
        'inventario_filtrado': [{'nombre': p['nombre'], 'precio': p['precio']} for p in ordenados]
    }
    return resultado

# === TESTS ===
try:
    data = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 15, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 30, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 50, 'stock': 0}
    ]
    resultado_esperado = {
        'producto_mas_barato': 'Mouse', 
        'inventario_filtrado': [{'nombre': 'Mouse', 'precio': 15}, {'nombre': 'Teclado', 'precio': 30}, {'nombre': 'Monitor', 'precio': 200}]
    }
    assert procesar_inventario(data) == resultado_esperado, "Error: la lógica de filtrado u ordenamiento es incorrecta."
    assert procesar_inventario([])['producto_mas_barato'] == None, "Error: no maneja correctamente listas vacías."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")