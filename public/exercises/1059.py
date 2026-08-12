# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, buscar y retornar los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para ordenar, y luego extraer los nombres de los elementos que cumplan con el presupuesto.

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
    inventario_1 = [
        {'nombre': 'Arroz', 'precio': 15.0, 'stock': 5},
        {'nombre': 'Carne', 'precio': 50.0, 'stock': 0},
        {'nombre': 'Leche', 'precio': 10.0, 'stock': 10},
        {'nombre': 'Huevos', 'precio': 12.0, 'stock': 2}
    ]
    
    assert procesar_inventario(inventario_1, 15.0) == ['Leche', 'Huevos', 'Arroz'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_1, 5.0) == [], "Error: considera casos límites en tu lógica."
    
    inventario_2 = [
        {'nombre': 'Laptop', 'precio': 800.0, 'stock': 3},
        {'nombre': 'Mouse', 'precio': 25.0, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45.0, 'stock': 5}
    ]
    assert procesar_inventario(inventario_2, 50.0) == ['Mouse', 'Teclado'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")