# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre y precio), debes implementar una función que filtre los productos con un precio mayor a un valor dado, los ordene de menor a mayor precio y finalmente busque si existe un producto específico por nombre en la lista resultante.
# difficulty: Intermedio
# expected_output: True o False dependiendo de si el producto existe en la lista filtrada y ordenada.
# hint: Usa una lista por comprensión para filtrar, el método .sort() o sorted() para ordenar y un bucle o el operador 'in' para buscar.

# === SOLUTION ===
def procesar_inventario(productos, precio_minimo, nombre_buscado):
    filtrados = [p for p in productos if p['precio'] > precio_minimo]
    filtrados.sort(key=lambda x: x['precio'])
    nombres_filtrados = [p['nombre'] for p in filtrados]
    return nombre_buscado in nombres_filtrados

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Mouse', 'precio': 20},
        {'nombre': 'Monitor', 'precio': 200},
        {'nombre': 'Teclado', 'precio': 50}
    ]
    assert procesar_inventario(inventario, 30, 'Teclado') == True, "Error: El test 1 ha fallado."
    assert procesar_inventario(inventario, 100, 'Mouse') == False, "Error: Considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 1000, 'Laptop') == False, "Error: El caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")