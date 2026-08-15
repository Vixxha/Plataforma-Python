# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, buscar y retornar una lista solo con los nombres de aquellos productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter/map combinados con el método sorted() de Python para ordenar los diccionarios según una clave específica.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0 y precio <= presupuesto
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= presupuesto]
    # Ordenar los productos filtrados por precio de forma ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_ejemplo = [
        {'nombre': 'Arroz', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Pan', 'precio': 1.5, 'stock': 50},
        {'nombre': 'Leche', 'precio': 3.0, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 2.0, 'stock': 20},
        {'nombre': 'Carne', 'precio': 15.0, 'stock': 5}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 10.0) == ['Pan', 'Manzana'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 1.0) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 50.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")