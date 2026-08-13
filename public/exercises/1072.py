# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios con información de productos (nombre y precio), filtre aquellos que tengan un precio menor o igual a un presupuesto máximo, ordene los resultados de forma ascendente según su precio y devuelva una lista únicamente con los nombres de los productos ordenados.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Monitor']
# hint: Puedes usar list comprehensions o filter para la búsqueda/filtrado, la función sorted() con una función lambda para ordenar, y otra comprensión para extraer solo los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto_maximo):
    filtrados = [p for p in productos if p['precio'] <= presupuesto_maximo]
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200},
        {'nombre': 'Mouse', 'precio': 25},
        {'nombre': 'Monitor', 'precio': 200},
        {'nombre': 'Teclado', 'precio': 45},
        {'nombre': 'Impresora', 'precio': 150}
    ]
    
    assert filtrar_y_ordenar_productos(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 300) == ['Mouse', 'Teclado', 'Monitor', 'Impresora'], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")