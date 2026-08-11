# === METADATA ===
# title: Filtrado, Ordenamiento y Búsqueda de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea menor o igual a un presupuesto máximo, ordene los resultados de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate), y finalmente devuelva una lista con solo los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para la selección, el método sort() o la función sorted() con una clave múltiple (tupla) para el ordenamiento, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def procesar_productos(productos, presupuesto_max):
    filtrados = [p for p in productos if p['precio'] <= presupuesto_max]
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Arroz', 'precio': 25.0},
        {'nombre': 'Leche', 'precio': 15.0},
        {'nombre': 'Manzana', 'precio': 10.0},
        {'nombre': 'Carne', 'precio': 50.0},
        {'nombre': 'Pan', 'precio': 15.0}
    ]
    
    inventario_vacio = []
    
    assert procesar_productos(inventario, 20.0) == ['Manzana', 'Leche', 'Pan'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 5.0) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario_vacio, 100.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")