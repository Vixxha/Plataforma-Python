# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente busque el nombre del producto más barato de la lista resultante.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista usando la clave 'precio' y accede al índice 0 del resultado.

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
        {'nombre': 'Mouse', 'precio': 20, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2}
    ]
    assert buscar_producto_mas_barato(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert buscar_producto_mas_barato([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: debería retornar None si no hay stock."
    assert buscar_producto_mas_barato([{'nombre': 'B', 'precio': 50, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")