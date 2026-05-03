# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Primero usa una lista por comprensión para filtrar, luego el método sort() o la función sorted() con una llave lambda, y finalmente mapea para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Mouse", "precio": 20, "stock": 10},
        {"nombre": "Teclado", "precio": 50, "stock": 0},
        {"nombre": "Cable HDMI", "precio": 10, "stock": 2}
    ]
    # Caso: Ordenar por precio, filtrar stock > 0
    # Orden esperado tras filtro y ordenamiento por precio: Cable (10), Mouse (20), Monitor (200)
    assert procesar_inventario(inventario) == ['Cable HDMI', 'Mouse', 'Monitor'], "Error: el orden o filtrado es incorrecto."
    assert procesar_inventario([]) == [], "Error: el caso base de lista vacía falló."
    assert procesar_inventario([{"nombre": "A", "precio": 10, "stock": 0}]) == [], "Error: no se filtró correctamente el stock 0."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")