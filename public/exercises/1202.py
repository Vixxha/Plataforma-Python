# === METADATA ===
# title: Filtrar, Ordenar y Buscar Productos
# description: Escribe una función que reciba una lista de diccionarios (productos, donde cada uno tiene 'nombre' y 'precio'), filtre aquellos cuyo precio sea mayor o igual a un límite dado, los ordene de forma ascendente según su precio (y alfabéticamente por nombre en caso de empate) y finalmente busque y devuelva una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Camisa', 'Pantalón', 'Zapatos']
# hint: Puedes usar list comprehensions o filter para el filtrado, sorted con una función key basada en múltiples criterios para el ordenamiento, y otra comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_productos(productos, precio_minimo):
    # Filtrar productos por precio mínimo
    filtrados = [p for p in productos if p['precio'] >= precio_minimo]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(filtrados, key=lambda x: (x['precio'], x['nombre']))
    
    # Extraer únicamente los nombres
    resultado = [p['nombre'] for p in ordenados]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Zapatos', 'precio': 50.0},
        {'nombre': 'Gorra', 'precio': 15.0},
        {'nombre': 'Camisa', 'precio': 25.0},
        {'nombre': 'Pantalón', 'precio': 25.0},
        {'nombre': 'Calcetines', 'precio': 5.0}
    ]
    
    assert procesar_productos(inventario, 20.0) == ['Camisa', 'Pantalón', 'Zapatos'], "Error: el test 1 ha fallado."
    assert procesar_productos(inventario, 100.0) == [], "Error: considera casos límites en tu lógica."
    assert procesar_productos(inventario, 5.0) == ['Calcetines', 'Gorra', 'Camisa', 'Pantalón', 'Zapatos'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")