# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock menor a 5, los ordene por precio de menor a mayor y finalmente busque si existe un producto específico por nombre en la lista resultante. La función debe retornar el nombre del producto encontrado o None si no existe.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Usa una lista de comprensión para el filtro, el método .sort() o sorted() con una función lambda para el ordenamiento, y un bucle o condicional para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos, nombre_busqueda):
    filtrados = [p for p in productos if p['stock'] < 5]
    filtrados.sort(key=lambda x: x['precio'])
    
    for p in filtrados:
        if p['nombre'] == nombre_busqueda:
            return p['nombre']
    return None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 10},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 2},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 3},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 1}
    ]
    assert procesar_inventario(inventario, 'Teclado') == 'Teclado', "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 'Laptop') == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario, 'Camara') == None, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")