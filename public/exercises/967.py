# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista con únicamente los nombres de los primeros `n` productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con la función lambda para el ordenamiento por múltiples criterios o clave, y slicing para limitar la cantidad de resultados.

# === SOLUTION ===
def procesar_inventario(productos, n):
    productos_filtrados = [p for p in productos if p['stock'] > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    nombres = [p['nombre'] for p in productos_ordenados[:n]]
    return nombres

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 3}
    ]
    assert procesar_inventario(inv1, 2) == ['Laptop', 'Smartphone'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 5) == ['Laptop', 'Smartphone', 'Mouse'], "Error: considera casos límites en tu lógica."
    
    inv2 = [{'nombre': 'Monitor', 'precio': 300.0, 'stock': 0}]
    assert procesar_inventario(inv2, 1) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")