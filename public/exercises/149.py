# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y busca el nombre del primer producto que sea más barato.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Usa un filtro (o list comprehension) para el stock, el método .sort() o sorted() con una lambda para el precio, y extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2}
    ]
    # Filtramos stock > 0: Laptop, Mouse, Monitor. Ordenados: Mouse(20), Monitor(150), Laptop(800)
    assert procesar_inventario(inventario) == ['Mouse', 'Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso de lista vacía falló."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: no debe incluir productos sin stock."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")