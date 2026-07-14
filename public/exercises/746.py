# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock menor a 5, los ordene por precio de menor a mayor y devuelva solo los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Usa un filtro (o list comprehension) para el stock, luego utiliza el método .sort() o la función sorted() con una lambda para ordenar por precio.

# === SOLUTION ===
def filtrar_y_ordenar_inventario(productos):
    # Filtrar productos con stock menor a 5
    filtrados = [p for p in productos if p['stock'] < 5]
    # Ordenar por precio de menor a mayor
    filtrados.sort(key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in filtrados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 8},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 3}
    ]
    assert filtrar_y_ordenar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: el orden o filtrado es incorrecto."
    assert filtrar_y_ordenar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == ['A'], "Error: el caso con un solo elemento falló."
    assert filtrar_y_ordenar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 10}]) == [], "Error: no debería devolver elementos con stock alto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")