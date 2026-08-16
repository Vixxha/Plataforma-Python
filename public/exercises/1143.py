# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo, ordene el resultado de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista con los nombres de los productos filtrados y ordenados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar las funciones filter o listas por comprensión para el filtro, el método .sort() o la función sorted() con una clave múltiple (lambda) para ordenar, y otra comprensión de lista para extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 150},
        {"nombre": "Mouse", "precio": 25},
        {"nombre": "Teclado", "precio": 45},
        {"nombre": "Cable USB", "precio": 10},
        {"nombre": "Alfombrilla", "precio": 25}
    ]
    
    assert filtrar_ordenar_productos(inventario, 25) == ['Alfombrilla', 'Mouse', 'Teclado', 'Monitor'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(inventario, 100) == ['Monitor'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(inventario, 300) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")