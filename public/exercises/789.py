# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), debes: 1) Filtrar los productos con stock mayor a 0, 2) Ordenarlos por precio de menor a mayor, y 3) Implementar una búsqueda que devuelva el nombre del producto más barato dentro de esa lista filtrada.
# difficulty: Intermedio
# expected_output: "Teclado"
# hint: Utiliza la función filter() o una list comprehension para el filtrado, el método sort() o la función sorted() para el ordenamiento y accede al primer elemento del resultado.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    
    # Retornar el nombre del más barato si existen, sino None
    return disponibles[0]['nombre'] if disponibles else None

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Teclado", "precio": 30, "stock": 10},
        {"nombre": "Mouse", "precio": 50, "stock": 0},
        {"nombre": "Cable", "precio": 10, "stock": 2}
    ]
    assert procesar_inventario(inventario) == "Cable", "Error: el test 1 ha fallado."
    assert procesar_inventario([{"nombre": "A", "precio": 100, "stock": 0}]) == None, "Error: considera el caso sin stock."
    assert procesar_inventario([{"nombre": "B", "precio": 50, "stock": 1}]) == "B", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")