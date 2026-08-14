# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor al mínimo requerido, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pera', 'Plátano']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p['stock'] > stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    nombres = [p['nombre'] for p in ordenados]
    return nombres

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Pera', 'precio': 2.5, 'stock': 10},
        {'nombre': 'Manzana', 'precio': 1.2, 'stock': 15},
        {'nombre': 'Uva', 'precio': 4.0, 'stock': 2},
        {'nombre': 'Plátano', 'precio': 1.8, 'stock': 20}
    ]
    assert procesar_inventario(inv1, 5) == ['Manzana', 'Plátano', 'Pera'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 25) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")