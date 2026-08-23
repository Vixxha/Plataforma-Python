# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves "nombre", "precio" y "stock"). La función debe filtrar aquellos productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio (y en caso de empate, alfabéticamente por su nombre), y finalmente retornar una lista con los nombres de los primeros `n` productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted() con una clave múltiple (tupla) para el ordenamiento, y slicing para limitar la cantidad de elementos.

# === SOLUTION ===
def procesar_inventario(productos, n):
    productos_filtrados = [p for p in productos if p.get('stock', 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: (x['precio'], x['nombre']))
    resultado = [p['nombre'] for p in productos_ordenados[:n]]
    return resultado

# === TESTS ===
try:
    inventario_ejemplo = [
        {"nombre": "Mochila", "precio": 45.50, "stock": 10},
        {"nombre": "Cuaderno", "precio": 3.50, "stock": 0},
        {"nombre": "Lapicero", "precio": 1.20, "stock": 25},
        {"nombre": "Borrador", "precio": 1.20, "stock": 50},
        {"nombre": "Regla", "precio": 2.00, "stock": 5}
    ]
    
    assert procesar_inventario(inventario_ejemplo, 3) == ["Borrador", "Lapicero", "Regla"], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_ejemplo, 1) == ["Borrador"], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 2) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")