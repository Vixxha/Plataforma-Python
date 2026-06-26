# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos productos cuyo precio sea superior a 100.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Utiliza una lista de comprensión para el filtrado inicial y el método .sort() o la función sorted() con una expresión lambda para el ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock >= 5 y precio > 100
    filtrados = [p for p in productos if p['stock'] >= 5 and p['precio'] > 100]
    # Ordenar por precio
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Extraer nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Mouse", "precio": 20, "stock": 10},
        {"nombre": "Laptop", "precio": 800, "stock": 8},
        {"nombre": "Teclado", "precio": 50, "stock": 2},
        {"nombre": "Monitor", "precio": 150, "stock": 6}
    ]
    assert procesar_inventario(inventario) == ["Monitor", "Laptop"], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([{"nombre": "Barato", "precio": 50, "stock": 10}]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")