# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), debes filtrar aquellos con stock mayor a 0, ordenarlos de forma ascendente por precio y finalmente buscar el nombre del producto más barato que cumpla con la condición.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Usa la función sorted() con una expresión lambda para ordenar y el filtrado básico de listas o list comprehensions.

# === SOLUTION ===
def buscar_producto_mas_barato(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Retornar el nombre del primero (más barato) o None si está vacío
    return ordenados[0]['nombre'] if ordenados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 2}
    ]
    assert buscar_producto_mas_barato(inventario) == 'Teclado', "Error: el test 1 ha fallado."
    assert buscar_producto_mas_barato([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == None, "Error: considera casos límites en tu lógica."
    assert buscar_producto_mas_barato([{'nombre': 'C', 'precio': 50, 'stock': 1}, {'nombre': 'B', 'precio': 10, 'stock': 1}]) == 'B', "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")