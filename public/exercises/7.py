# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea menor a 500.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Utiliza una lista de comprensión para el filtro o la función filter(), el método sort() o la función sorted() para el ordenamiento, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de menor a mayor
    en_stock.sort(key=lambda x: x['precio'])
    
    # Filtrar nombres de productos con precio < 500
    resultado = [p['nombre'] for p in en_stock if p['precio'] < 500]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 600, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: El filtrado u ordenamiento no es correcto."
    assert procesar_inventario([{'nombre': 'CPU', 'precio': 1000, 'stock': 1}]) == [], "Error: Debería filtrar productos caros."
    assert procesar_inventario([]) == [], "Error: El caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función procesar_inventario no está definida. Verifica el nombre.")