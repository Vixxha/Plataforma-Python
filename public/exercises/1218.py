# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un valor mínimo dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista únicamente con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar listas de comprensión o filter() para la primera parte, el parámetro key de sorted() con una tupla para ordenamientos múltiples, y una comprensión final para extraer los nombres.

# === SOLUTION ===
def filtrar_ordenar_productos(productos, precio_minimo):
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    catalogo = [
        {'nombre': 'Zapatos', 'precio': 50},
        {'nombre': 'Gorra', 'precio': 15},
        {'nombre': 'Camisa', 'precio': 25},
        {'nombre': 'Pantalón', 'precio': 40},
        {'nombre': 'Corbata', 'precio': 15}
    ]
    
    assert filtrar_ordenar_productos(catalogo, 20) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_productos(catalogo, 15) == ['Corbata', 'Gorra', 'Camisa', 'Pantalón', 'Zapatos'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_productos(catalogo, 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")