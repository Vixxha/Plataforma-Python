# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los productos resultantes de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista con solo los nombres de los productos ordenados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar la función `filter` o una comprensión de lista para el filtrado, y la función `sorted` junto con una función `lambda` en el parámetro `key` para ordenar utilizando múltiples criterios.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inv = [
        {'nombre': 'Laptop', 'precio': 800},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Monitor', 'precio': 150},
        {'nombre': 'Audífonos', 'precio': 25}
    ]
    assert filtrar_ordenar_productos(inv, 30) == ['Teclado', 'Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(inv, 20) == ['Audífonos', 'Mouse', 'Teclado', 'Monitor', 'Laptop'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(inv, 1000) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")