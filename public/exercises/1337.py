# === METADATA ===
# title: Gestión y Filtrado de Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (con claves 'nombre', 'precio' y 'stock'), filtre aquellos que tengan un stock mayor a cero, ordene los resultados de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre), y finalmente busque y devuelva una lista únicamente con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Manzana', 'Pan', 'Leche']
# hint: Puedes usar list comprehensions o filter para el filtrado, la función sorted con una clave múltiple (tupla) para el ordenamiento, y asegurarte de aplicar cada paso secuencialmente.

# === SOLUTION ===
def filtrar_ordenar_y_buscar(productos, presupuesto):
    # Filtrar productos con stock mayor a 0
    en_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(en_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {'nombre': 'Manzana', 'precio': 1.5, 'stock': 10},
        {'nombre': 'Carne', 'precio': 10.0, 'stock': 0},
        {'nombre': 'Pan', 'precio': 1.0, 'stock': 5},
        {'nombre': 'Leche', 'precio': 1.2, 'stock': 8},
        {'nombre': 'Queso', 'precio': 5.0, 'stock': 2}
    ]
    
    assert filtrar_ordenar_y_buscar(inventario, 2.0) == ['Pan', 'Leche', 'Manzana'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_y_buscar(inventario, 0.5) == [], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_y_buscar(inventario, 10.0) == ['Pan', 'Leche', 'Manzana', 'Queso'], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")