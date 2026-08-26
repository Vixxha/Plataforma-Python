# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente, y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para eliminar el stock en 0, la función sorted() con una función lambda para ordenar por precio, y otra comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_disponibles = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Carne', 'precio': 10.0, 'stock': 0},
        {'nombre': 'Leche', 'precio': 2.0, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 0.8, 'stock': 20}
    ]
    assert procesar_inventario(inv1) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 2}
    ]
    assert procesar_inventario(inv2) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")