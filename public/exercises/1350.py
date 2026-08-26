# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la comprensión de listas o funciones filter y sorted combinadas para procesar los datos paso a paso.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0 y precio <= presupuesto
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= presupuesto]
    # Ordenar los productos filtrados por precio de forma ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Extraer y retornar solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Monitor', 'precio': 150.0, 'stock': 5},
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 15.0, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 45.0, 'stock': 4}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 50.0) == ['Teclado', 'Audífonos'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 200.0) == ['Teclado', 'Audífonos', 'Monitor'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_ejemplo, 10.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")