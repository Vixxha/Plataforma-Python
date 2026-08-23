# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre si hay empates) y finalmente devuelva una lista únicamente con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Monitor', 'Laptop']
# hint: Puedes usar la función `filter()` o una comprensión de listas, luego el método `sorted()` con una tupla como clave de ordenamiento, y finalmente extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 15},
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Monitor', 'precio': 200},
        {'nombre': 'Cable', 'precio': 15}
    ]
    
    assert filtrar_ordenar_productos(inventario, 40) == ['Teclado', 'Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(inventario, 1000) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(inventario, 15) == ['Cable', 'Mouse', 'Teclado', 'Monitor', 'Laptop'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")