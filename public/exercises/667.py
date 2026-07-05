# === METADATA ===
# title: Gestión de Inventario Electrónico
# description: Dada una lista de diccionarios que representan productos (nombre, precio, stock), filtra aquellos con stock mayor a 0, ordénalos por precio de menor a mayor y devuelve una lista con los nombres de los productos cuyo precio sea menor a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Mouse', 'Teclado']
# hint: Usa un filtro (o list comprehension) para el stock, el método .sort() con una función lambda para el precio, y otro filtro para el presupuesto.

# === SOLUTION ===
def filtrar_y_ordenar_productos(productos, presupuesto):
    # Filtrar stock > 0
    disponibles = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio
    disponibles.sort(key=lambda x: x['precio'])
    
    # Filtrar por presupuesto y extraer solo nombres
    resultado = [p['nombre'] for p in disponibles if p['precio'] < presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Monitor', 'precio': 200, 'stock': 5},
        {'nombre': 'Mouse', 'precio': 20, 'stock': 10},
        {'nombre': 'Teclado', 'precio': 50, 'stock': 2},
        {'nombre': 'Webcam', 'precio': 80, 'stock': 0}
    ]
    assert filtrar_y_ordenar_productos(inventario, 60) == ['Mouse', 'Teclado'], "Error: el test 1 ha fallado."
    assert filtrar_y_ordenar_productos(inventario, 10) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_y_ordenar_productos(inventario, 300) == ['Mouse', 'Teclado', 'Monitor'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")