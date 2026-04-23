# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dada una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock menor a 5, ordena los resultados restantes por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea superior a 500.
# difficulty: Intermedio
# expected_output: ['Laptop', 'Monitor']
# hint: Usa un ciclo for o list comprehension para filtrar, el método .sort() o sorted() con una expresión lambda para ordenar, y finalmente extrae los nombres.

# === SOLUTION ===
def procesar_inventario(productos):
    # Filtrar productos con stock >= 5
    stock_suficiente = [p for p in productos if p['stock'] >= 5]
    
    # Ordenar por precio de menor a mayor
    ordenados = sorted(stock_suficiente, key=lambda x: x['precio'])
    
    # Filtrar nombres con precio > 500
    resultado = [p['nombre'] for p in ordenados if p['precio'] > 500]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Laptop', 'precio': 1200, 'stock': 7},
        {'nombre': 'Teclado', 'precio': 45, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 600, 'stock': 8}
    ]
    assert procesar_inventario(inventario) == ['Monitor', 'Laptop'], "Error: el test 1 ha fallado."
    assert procesar_inventario([]) == [], "Error: debe manejar listas vacías."
    assert procesar_inventario([{'nombre': 'Barato', 'precio': 10, 'stock': 10}]) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")