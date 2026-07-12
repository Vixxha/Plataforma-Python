# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero filtra por stock, luego usa el método sort o sorted para ordenar por precio, y finalmente aplica un filtro de lista por precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de menor a mayor
    disponibles.sort(key=lambda x: x['precio'])
    
    # Filtrar nombres de productos por límite de precio
    resultado = [p['nombre'] for p in disponibles if p['precio'] < limite_precio]
    
    return resultado

# === TESTS ===
try:
    productos_ejemplo = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert procesar_inventario(productos_ejemplo, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(productos_ejemplo, 30) == ['Mouse'], "Error: considera casos límites en tu lógica."
    assert procesar_inventario([], 100) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")