# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con los nombres de los primeros `n` productos resultantes. Si hay productos con el mismo precio, mantén su orden relativo original.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Utiliza la comprensión de listas o la función filter para la condición, sorted con una función lambda para el ordenamiento, y rebanado de listas (slicing) para limitar a los primeros 'n' elementos.

# === SOLUTION ===
def procesar_inventario(productos, n):
    filtrados = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in ordenados[:n]]

# === TESTS ===
try:
    inv = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.0, "stock": 5},
        {"nombre": "Teclado", "precio": 45.0, "stock": 0},
        {"nombre": "Smartphone", "precio": 800.0, "stock": 3}
    ]
    assert procesar_inventario(inv, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 1) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")