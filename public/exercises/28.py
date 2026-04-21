# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve solo los nombres de aquellos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (o list comprehension), el método .sort() o sorted() con un parámetro 'key' y luego extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # Filtrar por precio y extraer nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] < limite_precio]
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 2}
    ]
    assert procesar_inventario(inventario, 100) == ['Teclado', 'Webcam'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: considera casos límites donde ningún producto cumple el precio."
    assert procesar_inventario([], 500) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")