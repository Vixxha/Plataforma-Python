# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente busque el nombre del producto más barato que cumpla con la condición. Si no hay productos, retorna None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Primero usa una lista por comprensión para filtrar, luego el método sort() o la función sorted() para ordenar, y finalmente accede al primer elemento.

# === SOLUTION ===
def buscar_producto_mas_barato(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    if not disponibles:
        return None
    
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 45, 'stock': 2}
    ]
    assert buscar_producto_mas_barato(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert buscar_producto_mas_barato([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: debería retornar None si no hay stock."
    assert buscar_producto_mas_barato([{'nombre': 'X', 'precio': 500, 'stock': 1}]) == 'X', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")