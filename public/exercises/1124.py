# === METADATA ===
# title: Filtrado, Ordenamiento y Búsqueda de Productos
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre' y 'precio'), filtre aquellos cuyo precio sea menor o igual a un presupuesto máximo, los ordene de forma ascendente según su precio (y alfabéticamente en caso de empate), y finalmente devuelva una lista únicamente con los nombres de dichos productos.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar las funciones integradas filter() o listas por comprensión para el filtro, el método .sort() con una clave múltiple (lambda) para ordenar, y otra comprensión de lista para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos, presupuesto_maximo):
    # Filtrar productos por presupuesto
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    filtrados.sort(key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer solo los nombres
    nombres = [p['nombre'] for p in filtrados]
    
    return nombres

# === TESTS ===
try:
    inv = [
        {'nombre': 'Televisor', 'precio': 300},
        {'nombre': 'Pan', 'precio': 2},
        {'nombre': 'Leche', 'precio': 2},
        {'nombre': 'Manzana', 'precio': 1}
    ]
    assert procesar_inventario(inv, 5) == ['Manzana', 'Leche', 'Pan'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inv, 1) == ['Manzana'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inv, 0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")