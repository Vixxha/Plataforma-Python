# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los restantes por precio de menor a mayor y devuelve una lista con los nombres de los productos filtrados y ordenados. Si el producto no existe o la lista está vacía, devuelve una lista vacía.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Primero usa una comprensión de lista para filtrar, luego utiliza el método .sort() o la función sorted() con una expresión lambda para ordenar por la clave 'precio'.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor o igual a 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio de menor a mayor
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 50},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Auriculares', 'precio': 30, 'stock': 20}
    ]
    
    resultado = procesar_inventario(inventario)
    assert resultado == ['Auriculares', 'Mouse', 'Monitor'], "Error: El filtrado u ordenamiento es incorrecto."
    assert procesar_inventario([]) == [], "Error: El caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'Barato', 'precio': 1, 'stock': 1}]) == [], "Error: Caso de exclusión total falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")