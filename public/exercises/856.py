# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar las funciones integradas filter() o listas por comprensión para el filtro, el parámetro 'key' en sort() o sorted() junto con una función lambda para el ordenamiento, y una comprensión de listas final para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Monitor', 'precio': 300.0, 'stock': 0},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Laptop', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Agotado', 'precio': 500.0, 'stock': 0},
        {'nombre': 'Barato', 'precio': 10.0, 'stock': 5}
    ]
    assert procesar_inventario(inv2) == ['Barato'], "Error: considera casos límites en tu lógica."
    
    assert procesar_inventario([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")