# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa una lista de comprensión para filtrar el stock, el método .sort() o sorted() con una función lambda para ordenar, y finalmente recorre la lista para extraer los nombres que cumplen la condición de precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio ascendente
    disponibles.sort(key=lambda x: x['precio'])
    # Filtrar nombres con precio menor al límite
    resultado = [p['nombre'] for p in disponibles if p['precio'] < limite_precio]
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 200, "stock": 5},
        {"nombre": "Mouse", "precio": 20, "stock": 10},
        {"nombre": "Teclado", "precio": 50, "stock": 2},
        {"nombre": "Cable", "precio": 10, "stock": 0}
    ]
    assert procesar_inventario(inventario, 60) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 15) == [], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")