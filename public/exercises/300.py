# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), filtra los productos con precio mayor a 50, ordénalos alfabéticamente por nombre y devuelve el resultado. Además, implementa una búsqueda que retorne el precio de un producto específico por nombre.
# difficulty: Intermedio
# expected_output: {'filtrados_y_ordenados': [{'nombre': 'Laptop', 'precio': 800}, {'nombre': 'Monitor', 'precio': 150}], 'precio_teclado': 25}
# hint: Usa 'sorted()' con una función lambda para el ordenamiento y una comprensión de listas para el filtro. Para la búsqueda, puedes iterar la lista o usar un diccionario de búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, nombre_busqueda):
    # Filtrar productos > 50
    filtrados = [p for p in productos if p['precio'] > 50]
    # Ordenar alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: x['nombre'])
    # Búsqueda de precio
    precio_buscado = next((p['precio'] for p in productos if p['nombre'] == nombre_busqueda), None)
    
    return {"filtrados_y_ordenados": ordenados, "precio_buscado": precio_buscado}

# === TESTS ===
try:
    data = [
        {"nombre": "Mouse", "precio": 20},
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Teclado", "precio": 25},
        {"nombre": "Laptop", "precio": 800}
    ]
    resultado = procesar_inventario(data, "Teclado")
    
    assert resultado["filtrados_y_ordenados"] == [{'nombre': 'Laptop', 'precio': 800}, {'nombre': 'Monitor', 'precio': 150}], "Error: El filtrado u ordenamiento es incorrecto."
    assert resultado["precio_buscado"] == 25, "Error: La búsqueda falló."
    assert procesar_inventario(data, "Inexistente")["precio_buscado"] == None, "Error: El caso de búsqueda inexistente falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")