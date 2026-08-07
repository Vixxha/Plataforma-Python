# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los primeros N productos resultantes (donde N es un parámetro dado).
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, el método sort() o la función sorted() con una función lambda para el ordenamiento, y slicing para limitar la cantidad de resultados.

# === SOLUTION ===
def procesar_inventario(productos, limite):
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_disponibles, key=lambda x: x['precio'], reverse=True)
    return [p['nombre'] for p in productos_ordenados[:limite]]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 3},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 5}
    ]
    
    assert procesar_inventario(inventario, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 1) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 2) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")