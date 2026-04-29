# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (con claves 'nombre', 'precio' y 'stock'), crea una función que: 1. Filtre los productos con stock mayor a 0, 2. Ordene los resultados de menor a mayor precio, y 3. Devuelva únicamente los nombres de los productos resultantes.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado', 'Monitor']
# hint: Usa una lista de comprensión o filter() para la condición, el método sort() o sorted() con una función lambda para ordenar, y una lista de comprensión para extraer los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtramos productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenamos por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    
    # Extraemos solo los nombres
    return [p['nombre'] for p in disponibles]

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 0},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 2}
    ]
    # Test: Los productos con stock 0 deben desaparecer y ordenarse por precio
    assert procesar_inventario(inventario) == ['Mouse', 'Webcam', 'Monitor'], "Error: El filtrado u ordenamiento es incorrecto."
    
    inventario_vacio = [{'nombre': 'PC', 'precio': 1000, 'stock': 0}]
    assert procesar_inventario(inventario_vacio) == [], "Error: No se manejó correctamente el caso de stock vacío."
    
    inventario_iguales = [{'nombre': 'A', 'precio': 10, 'stock': 1}, {'nombre': 'B', 'precio': 10, 'stock': 1}]
    assert procesar_inventario(inventario_iguales) == ['A', 'B'], "Error: El orden debe mantenerse estable con precios iguales."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")