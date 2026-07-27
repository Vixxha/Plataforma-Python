# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos ordenados que cumplan con la condición.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para la condición, la función sorted() con una función lambda para ordenar por 'precio', y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Mochila", "precio": 45.5, "stock": 5},
        {"nombre": "Lapicero", "precio": 1.2, "stock": 100},
        {"nombre": "Borrador", "precio": 0.5, "stock": 0},
        {"nombre": "Cuaderno", "precio": 3.5, "stock": 10}
    ]
    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Agotado", "precio": 10.0, "stock": 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "ItemB", "precio": 10.0, "stock": 2},
        {"nombre": "ItemA", "precio": 5.0, "stock": 1}
    ]
    assert procesar_inventario(inv3) == ['ItemA', 'ItemB'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")