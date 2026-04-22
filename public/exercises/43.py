# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los restantes por precio de forma ascendente y busca el producto más barato entre los filtrados.
# difficulty: Intermedio
# expected_output: {'nombre': 'Teclado', 'precio': 25, 'stock': 10}
# hint: Usa un filtro (list comprehension o filter) para descartar los productos, luego ordena la lista resultante con el método .sort() o sorted() usando una lambda como clave.

# === SOLUTION ===
def procesar_inventario(productos):
    # 1. Filtrar productos con stock >= 5
    filtrados = [p for p in productos if p['stock'] >= 5]
    
    # 2. Ordenar por precio de forma ascendente
    filtrados.sort(key=lambda x: x['precio'])
    
    # 3. Retornar el producto más barato (el primero tras ordenar) o None si no hay
    return filtrados[0] if filtrados else None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 2},
        {'nombre': 'Mouse', 'precio': 50, 'stock': 20},
        {'nombre': 'Teclado', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 3}
    ]
    assert procesar_inventario(inventario) == {'nombre': 'Teclado', 'precio': 25, 'stock': 10}, "Error: el test 1 ha fallado."
    assert procesar_inventario([{'nombre': 'A', 'precio': 10, 'stock': 1}]) == None, "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{'nombre': 'B', 'precio': 5, 'stock': 10}]) == {'nombre': 'B', 'precio': 5, 'stock': 10}, "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")