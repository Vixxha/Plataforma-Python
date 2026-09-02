# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock mayor a cero, los ordene de forma ascendente según su precio (y en caso de empate, alfabéticamente por nombre) y finalmente busque y devuelva una lista solo con los nombres de los productos cuyo precio sea menor o igual a un presupuesto dado.
# difficulty: Intermedio
# expected_output: ['Lapicero', 'Cuaderno', 'Mochila']
# hint: Utiliza list comprehensions o filter para la condición de stock, la función sorted con una clave múltiple (lambda) para el ordenamiento, y luego extrae los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_y_buscar(productos, presupuesto):
    # Filtrar productos con stock mayor a 0
    con_stock = [p for p in productos if p.get('stock', 0) > 0]
    
    # Ordenar por precio ascendente y luego por nombre alfabéticamente
    ordenados = sorted(con_stock, key=lambda x: (x['precio'], x['nombre']))
    
    # Filtrar por presupuesto y extraer solo los nombres
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Mochila", "precio": 45.50, "stock": 5},
        {"nombre": "Cuaderno", "precio": 12.00, "stock": 10},
        {"nombre": "Borrador", "precio": 1.50, "stock": 0},
        {"nombre": "Lapicero", "precio": 1.50, "stock": 25},
        {"nombre": "Laptop", "precio": 800.00, "stock": 2}
    ]
    
    assert filtrar_ordenar_y_buscar(inventario, 20.0) == ['Lapicero', 'Cuaderno'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_y_buscar(inventario, 50.0) == ['Lapicero', 'Cuaderno', 'Mochila'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_y_buscar(inventario, 1.0) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")