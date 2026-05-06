# === METADATA ===
# title: Gestión de Inventario Inteligente
# description: Dada una lista de diccionarios que representan productos (con llaves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y retorne solo una lista con los nombres de los productos resultantes. Si no hay productos, retorna una lista vacía.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Utiliza la función filter() o una comprensión de listas para el filtrado, el método sort() o la función sorted() con una lambda para el ordenamiento, y finalmente una lista por comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    disponibles_ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Extraer solo los nombres
    return [p['nombre'] for p in disponibles_ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Leche', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Pan', 'precio': 1.2, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 0.5, 'stock': 20},
        {'nombre': 'Carne', 'precio': 5.0, 'stock': 0}
    ]
    assert procesar_inventario(inventario) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")