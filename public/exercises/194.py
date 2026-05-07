# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que: 1. Filtre los productos con stock mayor a 0, 2. Ordene los resultados por precio de menor a mayor, y 3. Devuelva una lista solo con los nombres de los productos filtrados.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Puedes usar el método .sort() con una función lambda como 'key' o la función sorted(), y recuerda usar una lista de comprensión para el filtrado.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 5}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 0}]) == [], "Error: el caso de stock cero debe excluirse."
    assert procesar_inventario([{'nombre': 'C', 'precio': 30, 'stock': 1}, {'nombre': 'B', 'precio': 10, 'stock': 2}]) == ['B', 'C'], "Error: el ordenamiento por precio falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")