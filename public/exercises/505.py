# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los primeros 3 productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Usa un filtro (o list comprehension) para el stock, el método .sort() o sorted() con una función lambda para el precio, y el slicing [:3] para obtener los elementos.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados[:3]]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Impresora', 'precio': 200, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 1}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado', 'Webcam'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: el caso con stock 0 debe filtrarse."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 1}, {'nombre': 'A', 'precio': 1, 'stock': 1}]) == ['A', 'B'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")