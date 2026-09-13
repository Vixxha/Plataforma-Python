# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes. Si dos productos tienen el mismo precio, mantén su orden relativo original (o alphabetico según el nombre si es necesario, pero usa un ordenamiento estable).
# difficulty: Intermedio
# expected_output: ['Laptop', 'Mouse', 'Teclado']
# hint: Puedes usar la función filter() o una comprensión de lista para filtrar, el método .sort() o sorted() con la función lambda para ordenar, y otra comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Teclado", "precio": 45.5, "stock": 10},
        {"nombre": "Monitor", "precio": 150.0, "stock": 0},
        {"nombre": "Laptop", "precio": 999.99, "stock": 3},
        {"nombre": "Mouse", "precio": 25.0, "stock": 15}
    ]
    assert procesar_inventario(inv1) == ['Laptop', 'Teclado', 'Mouse'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {"nombre": "Agotado", "precio": 500.0, "stock": 0},
        {"nombre": "Barato", "precio": 10.0, "stock": 5}
    ]
    assert procesar_inventario(inv2) == ['Barato'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")