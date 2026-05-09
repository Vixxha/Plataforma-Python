# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a cero, ordénalos por precio de forma ascendente y busca si existe un producto específico por su nombre.
# difficulty: Intermedio
# expected_output: {'filtrados_y_ordenados': [{'nombre': 'teclado', 'precio': 20, 'stock': 10}, {'nombre': 'monitor', 'precio': 150, 'stock': 5}], 'existe_producto': True}
# hint: Utiliza el método sorted() con una expresión lambda para el ordenamiento y una comprensión de listas para el filtrado.

# === SOLUTION ===
def gestionar_inventario(productos, nombre_busqueda):
    filtrados = [p for p in productos if p['stock'] > 0]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    existe = any(p['nombre'] == nombre_busqueda for p in productos)
    return {'filtrados_y_ordenados': ordenados, 'existe_producto': existe}

# === TESTS ===
try:
    data = [
        {'nombre': 'monitor', 'precio': 150, 'stock': 5},
        {'nombre': 'mouse', 'precio': 10, 'stock': 0},
        {'nombre': 'teclado', 'precio': 20, 'stock': 10}
    ]
    resultado = gestionar_inventario(data, 'mouse')
    assert resultado['filtrados_y_ordenados'] == [{'nombre': 'teclado', 'precio': 20, 'stock': 10}, {'nombre': 'monitor', 'precio': 150, 'stock': 5}], "Error: El filtrado u ordenamiento es incorrecto."
    assert resultado['existe_producto'] == True, "Error: La búsqueda de producto falló."
    assert gestionar_inventario(data, 'impresora')['existe_producto'] == False, "Error: Debería retornar False para un producto inexistente."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")