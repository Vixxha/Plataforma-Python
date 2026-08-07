# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (cada uno con 'nombre' y 'precio'), filtre aquellos que tengan un precio menor o igual a un límite dado, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente devuelva una lista únicamente con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar listas por comprensión o la función filter para la selección, el método sort() o la función sorted() con una clave múltiple (tupla) para el ordenamiento, y otra comprensión de lista para extraer los nombres.

# === SOLUTION ===
def procesar_productos(productos, precio_limite):
    filtrados = [p for p in productos if p['precio'] <= precio_limite]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Arroz', 'precio': 1200},
        {'nombre': 'Leche', 'precio': 800},
        {'nombre': 'Manzana', 'precio': 500},
        {'nombre': 'Pan', 'precio': 500},
        {'nombre': 'Carne', 'precio': 3000}
    ]
    
    assert procesar_productos(inventario, 1000) == ['Manzana', 'Pan', 'Leche'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 400) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 5000) == ['Manzana', 'Pan', 'Leche', 'Arroz', 'Carne'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")