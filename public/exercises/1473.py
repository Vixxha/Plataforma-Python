# === METADATA ===
# title: Filtrado, Búsqueda y Ordenamiento de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves "nombre", "precio" y "stock"), filtre aquellos que tengan un stock mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente retorne una lista únicamente con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar la función `filter` o listas por comprensión para filtrar, y la función `sorted` junto con una función `lambda` en el parámetro `key` para ordenar usando múltiples criterios (precio y luego nombre).

# === SOLUTION ===
def procesar_inventario(productos, stock_minimo):
    filtrados = [p for p in productos if p["stock"] >= stock_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x["precio"], x["nombre"]))
    return [p["nombre"] for p in ordenados]

# === TESTS ===
try:
    inv1 = [
        {"nombre": "Mochila", "precio": 45.0, "stock": 5},
        {"nombre": "Cuaderno", "precio": 15.0, "stock": 10},
        {"nombre": "Lapicero", "precio": 2.5, "stock": 50},
        {"nombre": "Borrador", "precio": 2.5, "stock": 2}
    ]
    assert procesar_inventario(inv1, 5) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv1, 100) == [], "Error: considera casos límites en tu lógica."
    
    inv2 = [
        {"nombre": "Z", "precio": 10.0, "stock": 10},
        {"nombre": "A", "precio": 10.0, "stock": 15}
    ]
    assert procesar_inventario(inv2, 5) == ['A', 'Z'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")