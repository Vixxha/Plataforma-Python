# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos de menor a mayor precio y devuelve una lista con los nombres de los productos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Primero filtra por stock, luego usa el método sort o sorted para ordenar, y finalmente recorre la lista para filtrar por precio.

# === SOLUTION ===
def procesar_inventario(productos, limite_precio):
    # Filtrar por stock mayor a 0
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    en_stock.sort(key=lambda x: x['precio'])
    
    # Buscar nombres de productos con precio menor al límite
    resultado = [p['nombre'] for p in en_stock if p['precio'] < limite_precio]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert procesar_inventario(inventario, 60) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario(inventario, 10) == [], "Error: debería devolver lista vacía si no hay productos bajo el precio."
    assert procesar_inventario([], 100) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")