# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dado una lista de diccionarios que representan productos (con llaves 'nombre', 'precio' y 'stock'), crea una función que filtre los productos con stock mayor a cero, los ordene de forma descendente por precio y finalmente busque el nombre del primer producto que cueste menos de 500. Si no existe tal producto, devuelve None.
# difficulty: Intermedio
# expected_output: "Teclado Mecánico"
# hint: Usa un list comprehension o filter() para el stock, el método .sort() con una función lambda para el ordenamiento y un bucle o next() para la búsqueda.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock mayor a 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma descendente
    disponibles.sort(key=lambda x: x['precio'], reverse=True)
    
    # Buscar el primero con precio menor a 500
    for p in disponibles:
        if p['precio'] < 500:
            return p['nombre']
            
    return None

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 25, 'stock': 10},
        {'nombre': 'Monitor', 'precio': 300, 'stock': 0},
        {'nombre': 'Teclado Mecánico', 'precio': 450, 'stock': 2}
    ]
    assert procesar_inventario(inventario) == "Teclado Mecánico", "Error: No se obtuvo el producto esperado."
    assert procesar_inventario([{'nombre': 'Caro', 'precio': 1000, 'stock': 5}]) == None, "Error: Debería devolver None si no hay productos baratos."
    assert procesar_inventario([]) == None, "Error: El caso de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")