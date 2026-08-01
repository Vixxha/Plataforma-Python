# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios con productos (que contienen 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio, y finalmente devuelva una lista con únicamente los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una función lambda para el ordenamiento por una clave específica, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'])
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
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 2}
    ]
    assert procesar_inventario(inv2) == ['Mouse'], "Error: considera casos límites en tu lógica."
    
    inv3 = []
    assert procesar_inventario(inv3) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")