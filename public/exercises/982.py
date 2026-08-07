# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves "nombre", "precio" y "stock"), filtre aquellos que tengan un stock mayor a cero, los ordene de forma ascendente según su precio y finalmente devuelva una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Puedes usar listas por comprensión o las funciones `filter` y `sorted` junto con funciones lambda para ordenar por una clave específica del diccionario.

# === SOLUTION ===
def procesar_inventario(productos):
    productos_filtrados = [p for p in productos if p.get("stock", 0) > 0]
    productos_ordenados = sorted(productos_filtrados, key=lambda x: x["precio"])
    return [p["nombre"] for p in productos_ordenados]

# === TESTS ===
try:
    inventario_1 = [
        {"nombre": "Mochila", "precio": 45.50, "stock": 5},
        {"nombre": "Cuaderno", "precio": 12.00, "stock": 10},
        {"nombre": "Borrador", "precio": 1.50, "stock": 0},
        {"nombre": "Lapicero", "precio": 2.50, "stock": 25}
    ]
    
    inventario_2 = [
        {"nombre": "Tablet", "precio": 300.0, "stock": 0},
        {"nombre": "Fundas", "precio": 15.0, "stock": 2}
    ]

    assert procesar_inventario(inventario_1) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_2) == ['Fundas'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")