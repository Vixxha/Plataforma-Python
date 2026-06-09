# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios con productos (nombre y precio), filtra los productos cuyo precio sea mayor a 50, ordénalos de menor a mayor precio y busca si un producto específico existe en la lista filtrada.
# difficulty: Intermedio
# expected_output: {'filtrados_ordenados': [{'nombre': 'Teclado', 'precio': 60}, {'nombre': 'Monitor', 'precio': 150}], 'encontrado': True}
# hint: Usa una lista de comprensión para filtrar, el método .sort() o sorted() con una función lambda para ordenar, y una búsqueda simple para verificar la existencia.

# === SOLUTION ===
def gestionar_inventario(productos, precio_minimo, nombre_busqueda):
    filtrados = [p for p in productos if p['precio'] > precio_minimo]
    filtrados.sort(key=lambda x: x['precio'])
    encontrado = any(p['nombre'] == nombre_busqueda for p in filtrados)
    return {'filtrados_ordenados': filtrados, 'encontrado': encontrado}

# === TESTS ===
try:
    data = [{'nombre': 'Mouse', 'precio': 20}, {'nombre': 'Monitor', 'precio': 150}, {'nombre': 'Teclado', 'precio': 60}]
    resultado = gestionar_inventario(data, 50, 'Teclado')
    assert resultado['encontrado'] == True, "Error: el test 1 ha fallado."
    assert resultado['filtrados_ordenados'][0]['precio'] == 60, "Error: el ordenamiento falló."
    assert gestionar_inventario(data, 200, 'Mouse')['encontrado'] == False, "Error: el filtro no excluyó correctamente."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")