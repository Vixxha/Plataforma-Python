# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de los primeros N productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para el ordenamiento por precio, y slicing para limitar la cantidad de resultados.

# === SOLUTION ===
def procesar_inventario(productos, limite):
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    resultado = [p['nombre'] for p in productos_ordenados[:limite]]
    return resultado

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inv1, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 1) == ['Laptop'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'Agotado', 'precio': 100.0, 'stock': 0}], 5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")