# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor o igual a un valor mínimo dado, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar list comprehensions o filter para el filtro, la función sorted con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    productos_filtrados = [p for p in productos if p['stock'] >= stock_minimo]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Monitor', 'precio': 300.0, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 8}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 5) == ['Laptop', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 15) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 2) == ['Laptop', 'Monitor', 'Teclado', 'Mouse'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")