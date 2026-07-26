# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, buscar y retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted() con una función lambda para ordenar, y volver a filtrar para la selección final por presupuesto.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Arroz', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Manzana', 'precio': 3.5, 'stock': 50},
        {'nombre': 'Carne', 'precio': 120.0, 'stock': 0},
        {'nombre': 'Pan', 'precio': 2.0, 'stock': 20},
        {'nombre': 'Leche', 'precio': 5.0, 'stock': 15}
    ]
    
    assert procesar_inventario(inventario_prueba, 10.0) == ['Pan', 'Leche', 'Manzana'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba, 1.0) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 50.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")