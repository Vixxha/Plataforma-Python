# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, buscar y retornar una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una función lambda para ordenar, y recorrer el resultado para extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_inventario(productos, presupuesto):
    # Filtrar productos con stock > 0
    en_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    
    # Filtrar y extraer los nombres de los que están dentro del presupuesto
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Carne', 'precio': 15.5, 'stock': 5},
        {'nombre': 'Pan', 'precio': 1.2, 'stock': 10},
        {'nombre': 'Leche', 'precio': 2.5, 'stock': 0},
        {'nombre': 'Manzana', 'precio': 0.8, 'stock': 20},
        {'nombre': 'Queso', 'precio': 5.0, 'stock': 3}
    ]
    
    assert filtrar_ordenar_inventario(inventario, 5.0) == ['Manzana', 'Pan', 'Queso'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_inventario(inventario, 1.0) == ['Manzana'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_inventario(inventario, 0.5) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")