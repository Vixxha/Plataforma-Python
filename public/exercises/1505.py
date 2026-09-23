# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente retornar una lista con los nombres de los productos que cumplan con la búsqueda de un precio máximo especificado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para eliminar el stock en cero, la función sorted() con una clave múltiple (lambda) para ordenar, y luego filtrar por el precio máximo.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, precio_maximo):
    # Filtrar productos con stock > 0 y precio menor o igual al máximo
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= precio_maximo]
    
    # Ordenar primero por precio (ascendente) y luego por nombre (alfabéticamente)
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Retornar únicamente una lista con los nombres de los productos
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 2},
        {'nombre': 'Auriculares', 'precio': 25.5, 'stock': 8}
    ]
    
    assert filtrar_y_ordenar_productos(inventario, 100.0) == ['Auriculares', 'Mouse'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 200.0) == ['Auriculares', 'Mouse', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")