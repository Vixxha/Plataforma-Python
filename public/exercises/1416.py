# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a 0, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted() con una función lambda para ordenar por precio, y luego extraer los nombres de los que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto):
    # Filtrar productos con stock mayor a 0 y cuyo precio sea menor o igual al presupuesto
    productos_filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= presupuesto]
    
    # Ordenar los productos filtrados por precio de forma ascendente
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x['precio'])
    
    # Extraer y retornar solo los nombres
    return [p['nombre'] for p in productos_ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200.0, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 3},
        {'nombre': 'Audífonos', 'precio': 30.0, 'stock': 8}
    ]
    
    assert filtrar_y_ordenar_productos(inventario, 50.0) == ['Mouse', 'Audífonos'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 200.0) == ['Mouse', 'Audífonos', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")