# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos que tengan un precio inferior a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse']
# hint: Usa un filtro (list comprehension o filter), luego ordena la lista resultante con sorted() usando una función lambda como key, y finalmente extrae los nombres.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto):
    # Filtrar stock > 0 y precio < presupuesto
    filtrados = [p for p in productos if p['stock'] > 0 and p['precio'] < presupuesto]
    # Ordenar por precio
    ordenados = sorted(filtrados, key=lambda x: x['precio'])
    # Retornar lista de nombres
    return [p['nombre'] for p in ordenados]

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