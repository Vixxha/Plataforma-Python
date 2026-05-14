# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos que cuestan menos de 500.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con sorted() o el método .sort() usando una llave lambda, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente
    disponibles.sort(key=lambda x: x['precio'])
    
    # Filtrar nombres de productos con precio < 500
    resultado = [p['nombre'] for p in disponibles if p['precio'] < 500]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 800, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 150, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 300, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 600, 'stock': 0}
    ]
    assert procesar_inventario(inventario) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: el caso base falló."
    assert procesar_inventario([{'nombre': 'USB', 'precio': 50, 'stock': 0}]) == [], "Error: considera casos límites en tu lógica."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")