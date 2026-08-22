# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes. Si hay productos con el mismo precio, mantén su orden relativo original.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar la función filter (o una comprensión de listas) para el filtrado, la función sorted con una función lambda como clave para el ordenamiento, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Mouse", "precio": 25.5, "stock": 10},
        {"nombre": "Laptop", "precio": 1200.0, "stock": 2},
        {"nombre": "Teclado", "precio": 45.0, "stock": 0},
        {"nombre": "Monitor", "precio": 300.0, "stock": 5}
    ]
    assert procesar_inventario(inv1) == ["Laptop", "Monitor", "Mouse"], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "A", "precio": 10, "stock": 0},
        {"nombre": "B", "precio": 20, "stock": 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {"nombre": "Libreta", "precio": 5.0, "stock": 100},
        {"nombre": "Bolígrafo", "precio": 1.5, "stock": 50}
    ]
    assert procesar_inventario(inv3) == ["Libreta", "Bolígrafo"], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")