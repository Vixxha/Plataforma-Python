# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos por precio de forma ascendente (y en caso de empate, alfabéticamente por nombre), y finalmente buscar y devolver una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Cuaderno', 'Lápiz', 'Mochila']
# hint: Puedes usar list comprehensions o filter para el filtrado inicial, la función sorted con una tupla de criterios para el ordenamiento, y recorrer la lista resultante para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_y_buscar(productos, presupuesto_maximo):
    # Filtrar productos con stock mayor a 0
    productos_disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    productos_ordenados = sorted(productos_disponibles, key=lambda x: (x['precio'], x['nombre']))
    
    # Buscar y extraer los nombres de los productos dentro del presupuesto máximo
    resultado = [p['nombre'] for p in productos_ordenados if p['precio'] <= presupuesto_maximo]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mochila', 'precio': 45.50, 'stock': 5},
        {'nombre': 'Lápiz', 'precio': 1.20, 'stock': 50},
        {'nombre': 'Cuaderno', 'precio': 3.50, 'stock': 0},
        {'nombre': 'Borrador', 'precio': 1.20, 'stock': 20},
        {'nombre': 'Laptop', 'precio': 800.00, 'stock': 2}
    ]
    
    inventario2 = [
        {'nombre': 'Zapatos', 'precio': 50.0, 'stock': 10},
        {'nombre': 'Camisa', 'precio': 25.0, 'stock': 0},
        {'nombre': 'Gorra', 'precio': 15.0, 'stock': 5}
    ]

    assert filtrar_ordenar_y_buscar(inventario, 5.0) == ['Borrador', 'Lápiz'], "Error: el test 1 ha fallado. Revisa el ordenamiento y filtro por stock."
    assert filtrar_ordenar_y_buscar(inventario2, 60.0) == ['Gorra', 'Zapatos'], "Error: considera casos límites en tu lógica y empates en precios."
    assert filtrar_ordenar_y_buscar(inventario, 1.0) == [], "Error: el caso base falló cuando ningún producto cumple el presupuesto."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")