# === METADATA ===
# title: Gestión y Búsqueda de Inventario
# description: Escribe una función que reciba una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'). La función debe filtrar los productos que tengan un stock mayor a cero, ordenarlos de forma ascendente según su precio y, finalmente, retornar una lista con los nombres de los productos que cumplan con un precio máximo especificado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Puedes usar las funciones filter() o comprensiones de lista para filtrar, y el parámetro key de sorted() para ordenar.

# === SOLUTION ===
def procesar_inventario(productos, precio_maximo):
    # Filtrar productos con stock > 0 y precio <= precio_maximo
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] <= precio_maximo]
    
    # Ordenar los productos filtrados por precio de forma ascendente
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    
    # Retornar únicamente una lista con los nombres de dichos productos
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario_prueba = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 0},
        {'nombre': 'Monitor', 'precio': 150, 'stock': 2}
    ]
    
    inventario_prueba_2 = [
        {'nombre': 'Silla', 'precio': 85, 'stock': 4},
        {'nombre': 'Escritorio', 'precio': 200, 'stock': 1},
        {'nombre': 'Lámpara', 'precio': 30, 'stock': 8}
    ]

    assert procesar_inventario(inventario_prueba, 100) == ['Mouse'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario_prueba_2, 100) == ['Lámpara', 'Silla'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario(inventario_prueba, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")