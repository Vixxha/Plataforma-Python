# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a 0, los ordene de menor a mayor precio y finalmente busque el nombre del producto más barato de la lista resultante.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa un filtro (list comprehension o filter), seguido del método sort o sorted para ordenar, y finalmente accede al primer elemento del índice.

# === SOLUTION ===
def buscar_producto_mas_barato(inventario):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in inventario if p['stock'] > 0]
    
    # Ordenar por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    
    # Retornar el nombre del primero si existe, sino None
    return disponibles[0]['nombre'] if disponibles else None

# === TESTS ===
try:
    productos = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2}
    ]
    assert buscar_producto_mas_barato(productos) == "Teclado", "Error: el test 1 ha fallado."
    assert buscar_producto_mas_barato([{'nombre': 'A', 'precio': 10, 'stock': 0}]) is None, "Error: considera casos límites donde no hay stock."
    assert buscar_producto_mas_barato([{'nombre': 'X', 'precio': 500, 'stock': 1}]) == "X", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")