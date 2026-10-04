# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con únicamente los nombres de los primeros N productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una función lambda para el ordenamiento por precio, y slicing para limitar la cantidad.

# === SOLUTION ===
def procesar_inventario(productos, limite):
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    nombres = [p['nombre'] for p in productos_ordenados[:limite]]
    return nombres

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 2}
    ]
    assert procesar_inventario(inv1, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'Libreta', 'precio': 5.0, 'stock': 50},
        {'nombre': 'Pluma', 'precio': 2.0, 'stock': 100},
        {'nombre': 'Mochila', 'precio': 40.0, 'stock': 0}
    ]
    assert procesar_inventario(inv2, 1) == ['Mochila'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3, 3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")