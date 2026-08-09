# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a cero, ordenarlos por su 'precio' de forma ascendente, y finalmente retornar una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento, y otra comprensión de listas para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_con_stock = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_con_stock, key=lambda x: x['precio'])
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Cuaderno', 'precio': 3.50, 'stock': 10},
        {'nombre': 'Borrador', 'precio': 0.75, 'stock': 0},
        {'nombre': 'Lapicero', 'precio': 1.20, 'stock': 25}
    ]
    
    inv2 = [
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 20.0, 'stock': 2}
    ]
    
    inv3 = []

    assert procesar_inventario(inv1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv2) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")