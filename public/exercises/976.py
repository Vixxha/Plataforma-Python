# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (del más barato al más caro), y finalmente retornar una lista únicamente con los nombres de esos productos ordenados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para la condición, la función sorted() con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_con_stock = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x['precio'])
    nombres_ordenados = [p['nombre'] for p in productos_ordenados]
    return nombres_ordenados

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80.0, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Mouse', 'Webcam', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'A', 'precio': 10, 'stock': 0},
        {'nombre': 'B', 'precio': 5, 'stock': 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Z', 'precio': 100, 'stock': 1},
        {'nombre': 'Y', 'precio': 50, 'stock': 3}
    ]
    assert procesar_inventario(inv3) == ['Y', 'Z'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")