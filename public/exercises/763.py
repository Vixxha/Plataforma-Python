# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve solo los nombres de los productos cuyo precio sea menor a 500.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (list comprehension o filter), la función sorted con un key lambda y un mapeo final para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar stock > 0 y precio < 500
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] < 500]
    # Ordenar por precio
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Retornar lista de nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 3}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == ['A'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 100, 'stock': 0}]) == [], "Error: el caso base falló (debe excluir stock 0)."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")