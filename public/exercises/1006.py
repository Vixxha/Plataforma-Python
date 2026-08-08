# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un 'stock' mayor a 0, ordenarlos de forma ascendente según su 'precio' y, finalmente, buscar y retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para ordenar, y finalmente extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_max):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inv = [
        {'nombre': 'Carne', 'precio': 15.5, 'stock': 5},
        {'nombre': 'Manzana', 'precio': 1.2, 'stock': 10},
        {'nombre': 'Pan', 'precio': 2.0, 'stock': 0},
        {'nombre': 'Leche', 'precio': 1.5, 'stock': 8}
    ]
    
    assert procesar_inventario(inv, 5.0) == ['Manzana', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 1.0) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 20.0) == ['Manzana', 'Leche', 'Carne'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")