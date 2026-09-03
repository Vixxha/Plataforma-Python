# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, buscar y retornar el nombre del producto más económico dentro de ese subconjunto filtrado. Si la lista está vacía o ningún producto cumple la condición, debe retornar None.
# difficulty: Intermedio
# expected_output: "Lápiz"
# hint: Primero filtra la lista usando una comprensión o filter(), luego usa la función sorted() o min() con una clave (key) basada en el precio.

# === SOLUTION ===
def procesar_inventario(productos):
    filtrados = [p for p in productos if p.get('stock', 0) > 0]
    if not filtrados:
        return None
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Cuaderno", "precio": 15.5, "stock": 5},
        {"nombre": "Lápiz", "precio": 2.0, "stock": 10},
        {"nombre": "Borrador", "precio": 1.5, "stock": 0}
    ]
    inventario_2 = [
        {"nombre": "Mochila", "precio": 45.0, "stock": 0},
        {"nombre": "Regla", "precio": 3.0, "stock": 2}
    ]
    inventario_3 = []

    assert procesar_inventario(inventario_1) == "Lápiz", "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_2) == "Regla", "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_3) is None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")