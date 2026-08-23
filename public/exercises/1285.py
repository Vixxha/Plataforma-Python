# === METADATA ===
# title: Gestión y Búsqueda de Productos en el Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos por su precio de forma ascendente (y en caso de empate, alfabéticamente por el nombre) y finalmente retornar una lista solo con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar listas de comprensión o filter para filtrar, la función sorted con una clave múltiple (tupla) para ordenar, y realizar una búsqueda lineal o filtrado final para el presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_max):
    # Filtrar productos con stock > 0
    con_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(con_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto máximo y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inventario_1 = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Teclado', 'precio': 25.5, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 25.5, 'stock': 0},
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 2},
        {'nombre': 'Audífonos', 'precio': 45.0, 'stock': 8}
    ]
    
    assert procesar_inventario(inventario_1, 50.0) == ['Teclado', 'Audífonos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_1, 200.0) == ['Teclado', 'Audífonos', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_1, 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")