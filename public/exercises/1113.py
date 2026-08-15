# === METADATA ===
# title: Gestión y Filtrado de Inventario de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan stock mayor a cero, ordenarlos por precio de forma ascendente y, finalmente, retornar una lista únicamente con los nombres de los productos que cumplan con la condición de búsqueda: cuyo precio sea menor o igual a un límite dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar list comprehensions o filter para eliminar el stock en 0, la función sorted() con una función lambda para ordenar por precio, y un bucle o filtro final para la búsqueda por límite de precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar productos con stock > 0 y precio <= limite_precio
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= limite_precio]
    # Ordenar por precio ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2}
    ]
    assert procesar_inventario(inv1, 200) == ['Mouse', 'Monitor'], "Error: el test 1 ha fallado."
    
    inv2 = [
        {'nombre': 'USB', 'precio': 10, 'stock': 50},
        {'nombre': 'Cable HDMI', 'precio': 15, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 30, 'stock': 5}
    ]
    assert procesar_inventario(inv2, 20) == ['USB'], "Error: considera casos límites en tu lógica."
    
    inv3 = [
        {'nombre': 'Tablet', 'precio': 300, 'stock': 0}
    ]
    assert procesar_inventario(inv3, 500) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")