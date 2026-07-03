# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a cero, los ordene de menor a mayor precio y finalmente retorne una lista solo con los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Utiliza la función filter() o una comprensión de listas para el filtrado, y el método sorted() con un parámetro 'key' para el ordenamiento.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    # Ordenar por precio de menor a mayor
    ordenados = sorted(disponibles, key=lambda x: x['precio'])
    # Extraer solo los nombres
    return [p['nombre'] for p in ordenados]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 3}
    ]
    # Caso: Ordenado y filtrado (Teclado tiene stock 0, debe excluirse)
    assert procesar_inventario(inventario) == ['Mouse', 'Webcam', 'Monitor'], "Error: el test 1 ha fallado."
    
    # Caso: Lista vacía
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    
    # Caso: Todos sin stock
    sin_stock = [{'nombre': 'A', 'precio': 10, 'stock': 0}]
    assert procesar_inventario(sin_stock) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")