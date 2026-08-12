# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos que tengan un precio menor o igual a un presupuesto máximo, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para la condición, el método sort() o la función sorted() con una clave múltiple (precio y nombre) para el ordenamiento, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos dentro del presupuesto
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    
    # Ordenar primero por precio (ascendente) y luego por nombre (alfabéticamente)
    filtrados_ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer únicamente los nombres de los productos
    return [p['nombre'] for p in filtrados_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Televisor', 'precio': 500},
        {'nombre': 'Manzana', 'precio': 2},
        {'nombre': 'Pan', 'precio': 2},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Leche', 'precio': 3}
    ]
    
    assert procesar_inventario(inventario_1, 5) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_1, 1), "Error: considera casos límites en tu lógica." == []
    
    inventario_2 = [
        {'nombre': 'Zapatos', 'precio': 50},
        {'nombre': 'Camisa', 'precio': 30},
        {'nombre': 'Gorra', 'precio': 30}
    ]
    assert procesar_inventario(inventario_2, 40) == ['Camisa', 'Gorra', 'Zapatos'] or procesar_inventario(inventario_2, 40) == ['Camisa', 'Gorra'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")