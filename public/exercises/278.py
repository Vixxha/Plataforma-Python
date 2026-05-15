# === METADATA ===
# title: Gestión de Inventario de Frutas
# description: Crea una función que tome una lista de diccionarios (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor a 10, los ordene alfabéticamente por nombre y busque si existe un producto específico tras el filtrado.
# difficulty: Intermedio
# expected_output: [{'nombre': 'Manzana', 'precio': 15}, {'nombre': 'Pera', 'precio': 20}]
# hint: Usa una lista de comprensión para el filtro, el método .sort() con una función lambda para ordenar y un bucle o 'any()' para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo, nombre_a_buscar):
    filtrados = [p for p in productos if p['precio'] > precio_minimo]
    filtrados.sort(key=lambda x: x['nombre'])
    
    existe = any(p['nombre'] == nombre_a_buscar for p in filtrados)
    
    return filtrados, existe

# === TESTS ===
try:
    inventario = [{'nombre': 'Pera', 'precio': 20}, {'nombre': 'Uva', 'precio': 5}, {'nombre': 'Manzana', 'precio': 15}]
    resultado_lista, resultado_bool = procesar_inventario(inventario, 10, 'Manzana')
    
    assert resultado_lista == [{'nombre': 'Manzana', 'precio': 15}, {'nombre': 'Pera', 'precio': 20}], "Error: El filtrado o el ordenamiento es incorrecto."
    assert resultado_bool == True, "Error: La búsqueda debería haber encontrado el elemento."
    
    _, test2 = procesar_inventario(inventario, 10, 'Uva')
    assert test2 == False, "Error: La búsqueda encontró un elemento que debería haber sido filtrado."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")