# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dada una lista de diccionarios que representan productos (nombre y precio), crea una función que filtre aquellos productos con precio mayor a un valor dado, los ordene de menor a mayor precio y retorne únicamente una lista con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pera']
# hint: Usa un ciclo o una lista de comprensión para filtrar, el método .sort() o sorted() para ordenar y finalmente una lista de comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] > precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Manzana', 'precio': 10},
        {'nombre': 'Arroz', 'precio': 5},
        {'nombre': 'Pera', 'precio': 15},
        {'nombre': 'Pan', 'precio': 2}
    ]
    assert procesar_inventario(inventario, 7) == ['Manzana', 'Pera'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 20) == [], "Error: debería retornar lista vacía si nada cumple la condición."
    assert procesar_inventario(inventario, 0) == ['Pan', 'Arroz', 'Manzana', 'Pera'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")