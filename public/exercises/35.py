# === METADATA ===
# title: Gestión de Inventario Tecnológico
# description: Dada una lista de diccionarios con productos (nombre, precio, stock), filtra los productos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de aquellos cuyo precio sea menor a un límite dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (o list comprehension) para el stock, luego sorted() con una llave lambda para el precio, y finalmente otra iteración para filtrar por presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto):
    # 1. Filtrar los que tienen stock
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # 2. Ordenar por precio de menor a mayor
    ordenados = sorted(en_stock, key=lambda x: x['precio'])
    
    # 3. Filtrar por presupuesto y extraer solo nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] < presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Laptop', 'precio': 1000, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Monitor', 'precio': 200, 'stock': 0}
    ]
    assert filtrar_y_ordenar_productos(inventario, 100) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 10) == [], "Error: considera casos donde ningún producto cumple el presupuesto."
    assert filtrar_y_ordenar_productos([], 500) == [], "Error: el caso base de lista vacía falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")