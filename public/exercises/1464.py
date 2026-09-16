# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para descartar stock en cero, la función sorted con una función lambda para ordenar por precio, y luego aplicar la búsqueda según el presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto_maximo):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inv = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 0},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 2}
    ]
    
    assert filtrar_y_ordenar_productos(inv, 100.0) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inv, 200.0) == ['Mouse', 'Teclado', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inv, 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")