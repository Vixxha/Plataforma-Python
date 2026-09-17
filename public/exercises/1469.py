# === METADATA ===
# title: Gestión y Búsqueda de Productos en un Inventario
# description: Escribe una función que reciba una lista de diccionarios representando productos (cada uno con 'nombre', 'precio' y 'stock'), filtre aquellos que tengan stock disponible mayor a cero, los ordene de forma ascendente según su precio y, finalmente, busque y devuelva una lista con los nombres de los productos cuyo precio sea menor o igual a un presupuesto máximo dado.
# difficulty: Intermedio
# expected_output: ['Teclado', 'Mouse', 'Audífonos']
# hint: Utiliza list comprehensions o filter para el filtrado, la función sorted() con una función lambda para el ordenamiento por precio, y recorre la lista resultante para extraer los nombres que cumplan con el presupuesto.

# === SOLUTION ===
def filtrar_ordenar_y_buscar_productos(productos, presupuesto_max):
    # Filtrar productos con stock > 0
    con_stock = [p for p in productos if p['stock'] > 0]
    
    # Ordenar por precio de forma ascendente
    ordenados = sorted(con_stock, key=lambda x: x['precio'])
    
    # Buscar y extraer nombres de productos dentro del presupuesto
    resultado = [p['nombre'] for p in ordenados if p['precio'] <= presupuesto_max]
    
    return resultado

# === TESTS ===
try:
    inventario = [
        {"nombre": "Monitor", "precio": 250, "stock": 5},
        {"nombre": "Mouse", "precio": 25, "stock": 10},
        {"nombre": "Teclado", "precio": 45, "stock": 0}, # Sin stock, debe filtrarse
        {"nombre": "Audífonos", "precio": 30, "stock": 8},
        {"nombre": "Laptop", "precio": 900, "stock": 2}
    ]
    
    assert filtrar_ordenar_y_buscar_productos(inventario, 50) == ['Mouse', 'Audífonos'], "Error: el test 1 ha fallado."
    assert filtrar_ordenar_y_buscar_productos(inventario, 1000) == ['Mouse', 'Audífonos', 'Monitor', 'Laptop'], "Error: considera casos límites en tu lógica."
    assert filtrar_ordenar_y_buscar_productos(inventario, 10) == [], "Error: el caso base falló."
except NameError:
    raise AssertionError("La función solicitada no está definida. Verifica el nombre.")