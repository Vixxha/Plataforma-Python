# === METADATA ===
# title: Gestión de Inventario Filtrado
# description: Dado una lista de diccionarios que representan productos (nombre, precio, stock), escribe una función que: 1) Filtre los productos que tengan un stock mayor a 0, 2) Ordene los resultados por precio de menor a mayor, y 3) Busque y devuelva solo el nombre del producto más barato de esa lista filtrada. Si la lista filtrada está vacía, devuelve None.
# difficulty: Intermedio
# expected_output: 'Teclado'
# hint: Primero usa una lista por comprensión o la función filter() para eliminar los productos sin stock. Luego, utiliza sorted() o .sort() con una función lambda para el ordenamiento.

# === SOLUTION ===
def obtener_producto_mas_economico(inventario):
    disponibles = [p for p in inventario if p['stock'] > 0]
    if not disponibles:
        return None
    
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    return ordenados[0]['nombre']

# === TESTS ===
try:
    inventario_test = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Teclado", "precio": 25, "stock": 10},
        {"nombre": "Mouse", "precio": 50, "stock": 0},
        {"nombre": "Cable", "precio": 10, "stock": 0}
    ]
    assert obtener_producto_mas_economico(inventario_test) == "Teclado", "Error: el test 1 ha fallado."
    assert obtener_producto_mas_economico([{"nombre": "A", "precio": 10, "stock": 0}]) == None, "Error: considera casos límites en tu lógica."
    assert obtener_producto_mas_economico([{"nombre": "X", "precio": 100, "stock": 1}]) == "X", "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")