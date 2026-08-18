# === METADATA ===
# title: Gestión de Inventario: Filtrar, Ordenar y Buscar
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a un valor mínimo dado, ordenarlos de forma descendente según su precio y, finalmente, retornar una lista únicamente con los nombres de estos productos resultantes.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Smartphone']
# hint: Puedes usar listas por comprensión o las funciones filter/sorted combinadas. Recuerda que para ordenar por un campo específico de un diccionario puedes usar una función lambda en el parámetro key de sorted().

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    # Filtrar productos con stock mayor al mínimo
    productos_filtrados = [p for p in productos if p['stock'] > stock_minimo]
    
    # Ordenar de forma descendente según el precio
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'], reverse=True)
    
    # Extraer únicamente los nombres
    nombres = [p['nombre'] for p in productos_ordenados]
    
    return nombres

# === TESTS ===
try:
    inv = [
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20.0, 'stock': 0},
        {'nombre': 'Smartphone', 'precio': 800.0, 'stock': 8}
    ]
    
    assert procesar_inventario(inv, 2) == ['Laptop', 'Smartphone', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 6) == ['Laptop', 'Smartphone'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 20) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")