# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos ordenados cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtro inicial, el método sorted() con una función lambda para el ordenamiento, y asegurarte de aplicar el límite de precio correctamente.

# === SOLUTION ===
def procesar_inventario(productos, precio_limite):
    disponibles = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    filtrados = [p['nombre'] for p in ordenados if p['precio'] <= precio_limite]
    return filtrados

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.5, 'stock': 5},
        {'nombre': 'Lapicero', 'precio': 1.2, 'stock': 100},
        {'nombre': 'Cuaderno', 'precio': 3.5, 'stock': 0},
        {'nombre': 'Borrador', 'precio': 0.5, 'stock': 20}
    ]
    assert procesar_inventario(inv1, 5.0) == ['Borrador', 'Lapicero'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 50.0) == ['Borrador', 'Lapicero', 'Mochila'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")