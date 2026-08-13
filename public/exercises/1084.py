# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento por clave, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_con_stock = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Carne', 'precio': 10.0, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 0.8, 'stock': 5},
        {'nombre': 'Leche', 'precio': 2.0, 'stock': 2}
    ]
    assert procesar_inventario(inv1) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'A', 'precio': 10, 'stock': 0},
        {'nombre': 'B', 'precio': 5, 'stock': 0}
    ]
    assert procesar_inventario(inv2) == [], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Laptop', 'precio': 800, 'stock': 1}
    ]
    assert procesar_inventario(inv3) == ['Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")