# === METADATA ===
# title: Gestión y Búsqueda de Productos en Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar aquellos productos que tengan stock mayor a cero, ordenarlos de forma ascendente por su precio y, finalmente, retornar una lista con los nombres de los productos que cumplan con un precio máximo especificado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar list comprehensions o funciones filter/sorted combinadas. Recuerda filtrar primero por stock, luego ordenar por precio y por último buscar o filtrar por el precio máximo.

# === SOLUTION ===
def filtrar_y_buscar_productos(productos, precio_maximo):
    # Filtrar productos con stock > 0 y precio menor o igual al máximo
    disponibles = [p for p in productos if p['stock'] > 0 and p['precio'] <= precio_maximo]
    # Ordenar por precio de forma ascendente
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # Retornar solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Audífonos', 'precio': 30, 'stock': 2}
    ]
    assert filtrar_y_buscar_productos(inventario, 50) == ['Mouse', 'Audífonos'], "Error: el test 1 ha fallado."
    assert filtrar_y_buscar_productos(inventario, 20) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_buscar_productos([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")